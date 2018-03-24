"""
PDFtk wrapper
"""

import re
import os
import shutil
import tempfile

from utils import run_command

__all__ = [
    'get_metadata',
    'set_metadata'
]


if os.getenv('PDFTK_PATH'):
    PDFTK_PATH = os.getenv('PDFTK_PATH')
else:
    PDFTK_PATH = '/usr/bin/pdftk'


def _split_meta(_str):
    if _str.startswith('InfoKey') or _str.startswith('InfoValue'):
        return _str.split(': ')[1]


def _split_toc(_str):
    keys_list = ['BookmarkTitle', 'BookmarkLevel', 'BookmarkPageNumber']
    keys_exists = any([_str.startswith(k) for k in keys_list])
    if keys_exists:
        return _str.split(': ')[1]


def _split_numbers_of_pages(_str):
    if _str.startswith('NumberOfPages'):
        return _str.split(': ')[1]


def _convert_to_underscore(_str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', _str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def _to_camelcase(_str):
    def camelcase():
        yield str.capitalize
        while True:
            yield str.capitalize

    c = camelcase()
    return "".join(next(c)(x) if x else '_' for x in _str.split("_"))


def _parse_metadata(_text):
    #  TODO: Set default keys
    parsed_list = [_split_meta(s) for s in _text.split('\n')]
    parsed_list = list(filter(None, parsed_list))
    _iter = iter(parsed_list)
    meta_dict = dict(zip(_iter, _iter))
    keywords = meta_dict.get('Keywords', None)
    meta_dict['Keywords'] = []
    if keywords:
        meta_dict['Keywords'] = [k.lstrip() for k in keywords.split(',')]
    return {_convert_to_underscore(k): v for k, v in meta_dict.items()}


def _add_toc_keys(item):
    return dict(title=item[0].lstrip(), level=int(item[1]), page=int(item[2]))


def _check_empty_title(s):
    if not s:
        return s
    if len(s) < 16 and 'BookmarkTitle' in s:
        return '%s  ' % s
    else:
        return s


def _parse_toc(_text):
    parsed_list = [_check_empty_title(s) for s in _text.split('\n')]
    parsed_list = list(map(_split_toc, parsed_list))
    parsed_list = list(map(_check_empty_title, parsed_list))
    parsed_list = list(filter(None, parsed_list))
    _iter = iter(parsed_list)
    return list(map(_add_toc_keys, zip(_iter, _iter, _iter)))


def _parse_number_of_pages(_text):
    parsed_list = [_split_numbers_of_pages(s) for s in _text.split('\n')]
    parsed_list = list(filter(None, parsed_list))
    return int(parsed_list[0])


def _check_value(key, value):
    if key == 'keywords':
        return ", ".join(value)
    return value


def _construct_metadata(metadata_dict) -> list:
    meta_tpl = (
        'InfoBegin\n'
        'InfoKey: {key}\n'
        'InfoValue: {value}\n'
    )
    toc_tpl = (
        'BookmarkBegin\n'
        'BookmarkTitle: {title}\n'
        'BookmarkLevel: {level}\n'
        'BookmarkPageNumber: {page}\n'
    )
    metadata_list = []

    meta = metadata_dict.get('metadata', None)
    if meta:
        for k, v in meta.items():
            metadata_list.append(
                meta_tpl.format(key=_to_camelcase(k),
                                value=_check_value(k, v))
            )

    toc = metadata_dict.get('toc', None)
    if toc:
        for item in toc:
            metadata_list.append(
                toc_tpl.format(title=item['title'],
                               level=item['level'],
                               page=item['page']))

    return metadata_list


def get_metadata(pdf_path) -> dict:
    """
    Get PDF metadata, TOC, count numbers of pages

    Metadata output format:

    {
        'toc': [
            {'page': 1, 'level': 1, 'title': 'One'},
            {'page': 2, 'level': 1, 'title': 'Two'}
        ],
        'number_of_pages': 19,
        'metadata': {
            'title': 'Hello',
            'creator': 'John Doe',
            'keywords': ['one', 'two', 'three'],
            'producer': 'John Galt',
            'subject': 'Bar',
            'creation_date': "D:20050829141305+03'00'",
            'author': 'Bob',
            'mod_date': "D:20130107184405+02'00'"
        }
    }

    :param pdf_path: dict
    :return: pdf metadata dict
    """

    root_path = os.path.dirname(pdf_path)
    temp_out = tempfile.mkstemp()[1]
    cmd = "%s %s dump_data_utf8 output %s" % (PDFTK_PATH, pdf_path, temp_out)

    try:
        run_command(cmd, shell=True, cwd=root_path)
        with open(temp_out, 'r') as f:
            metadata = f.read()
        os.remove(temp_out)
    except Exception as e:
        print(e)
    return dict(
        number_of_pages=_parse_number_of_pages(metadata),
        metadata=_parse_metadata(metadata),
        toc=_parse_toc(metadata))


def set_metadata(pdf_path, metadata_dict):
    """
    Update or insert metadata, TOC to PDF

    Metadata dict input format:

    {
        'toc': [
            {'page': 1, 'level': 1, 'title': 'One'},
            {'page': 2, 'level': 1, 'title': 'Two'}
        ],
        'metadata': {
            'title': 'Hello',
            'creator': 'John Doe',
            'keywords': ['one', 'two', 'three'],
            'producer': 'John Galt',
            'subject': 'Bar',
            'creation_date': "D:20050829141305+03'00'",
            'author': 'Johan',
            'mod_date': "D:20130107184405+02'00'"
        }
    }

    :param pdf_path: string
    :param metadata_dict: dict
    """

    root_path = os.path.dirname(pdf_path)
    temp_data = tempfile.mkstemp()[1]
    temp_out = tempfile.mkstemp()[1]

    cmd = "%s %s update_info_utf8 %s output %s" % (
        PDFTK_PATH, pdf_path, temp_data, temp_out)

    try:
        metadata_list = _construct_metadata(metadata_dict)
        with open(temp_data, 'w') as f:
            for item in metadata_list:
                f.write(item)

        run_command(cmd, shell=True, cwd=root_path)
        os.remove(temp_data)
        shutil.move(temp_out, pdf_path)
    except Exception as e:
        print(e)
