"""
Docsplit wrapper
"""

import os
import re
from itertools import chain

from utils import run_command


__all__ = [
    'split_pdf',
]


DOCSPLIT_PATH = '/usr/local/bin/docsplit'


def _get_path(root_path, img_path):
    return os.path.join(root_path, img_path)


def tryint(s):
    try:
        return int(s)
    except TypeError:
        return s


def _sort_files(_dir):
    return sorted(_dir, key=lambda x: (tryint(re.sub('\D', '', x)), x))


def _rename_files_list(root_path, sizes, docname, ex, splited_path) -> list:

    def _dir(path):
        size = {v: k for k, v in sizes.items()}[os.path.split(path)[-1]]
        files = _sort_files(os.listdir(path))
        c = 0
        for f in files:
            os.rename(
                os.path.join(path, f),
                os.path.join(path, '{name}-p{page}-{size}.{ex}'.format(
                    name=docname,
                    page=c,
                    size=size,
                    ex=ex,
                )))
            c += 1

        renamed = _sort_files(os.listdir(path))
        return [os.path.join(path, f) for f in renamed]
    paths = [os.path.join(root_path, splited_path, p) for p in sizes.values()]
    return list(chain(*map(_dir, paths)))


def split_pdf(pdf_path, splited_path, sizes, ex) -> list:
    """
    Split pdf document to images

    :param pdf_path: input pdf path
    :param sizes: dict of stings as {'thumbnail': 'x180', 'normal': 'x700', 'large': 'x1000'}
    :param ex: str as 'jpg'
    :return: list of img paths as ['/tmp/5566/0000.jpg', '/tmp/5566/0001.jpg',]

    """
    root_path = os.path.dirname(pdf_path)
    sizes_str = ','.join(sizes.values())
    doc_name = pdf_path.split('/')[-1].split('.')[0]
    cmd = "%s images %s --size %s --format %s --output %s" % (
        DOCSPLIT_PATH,
        pdf_path,
        sizes_str,
        ex,
        splited_path,
    )
    try:
        run_command(cmd, shell=True, cwd=root_path)
        return _rename_files_list(root_path, sizes, doc_name, ex, splited_path)

    except Exception as e:
        print(e)

