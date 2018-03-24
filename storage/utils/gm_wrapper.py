"""
Graphicmagik wrapper
"""

import os
from utils import run_command

__all__ = [
    'create_pdf',
    'get_preview_name',
]


GM_PATH = '/usr/bin/gm'


def _list_files(files_list):
    return " ".join(files_list)


def create_pdf(root_path, images_list, out_name):

    cmd = "%s convert %s %s" % (GM_PATH, _list_files(images_list), out_name)
    try:
        run_command(cmd, shell=True, cwd=root_path)
    except Exception as e:
        print(e)


def get_preview_name(source_document_path):
    path, name = os.path.split(source_document_path)
    document_name, document_ex = os.path.splitext(name)
    return os.path.join(path, '%s-preview%s' % (document_name, document_ex))
