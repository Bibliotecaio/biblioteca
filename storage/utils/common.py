import os
import asyncio
import mimetypes
import subprocess
import multiprocessing
from functools import wraps
from concurrent.futures import ThreadPoolExecutor

import yaml

from .sentry_client import sentry_client


__all__ = [
    'Config',
    'wraps_async',
    'run_command',
    'check_free_space',
    'check_mime_type',
]


class Config(object):
    """
    Usage:
    config = Config('config.yml')()
    """

    def __init__(self, path):
        self.path = path

    def __call__(self):
        with open(self.path, mode='r') as f:
            yml = f.read()
        return yaml.load(yml)


def wraps_async(f):
    @wraps(f)
    def wrapper(*args):
        pool = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(pool, f, *args)
        return future
    return wrapper


def _check_output(*popenargs, **kwargs):
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise subprocess.CalledProcessError(retcode, cmd)
    return output


def run_command(command, shell=False, cwd=None):
    """
    Run a system command and yield output
    """
    p = _check_output(command, shell=shell, cwd=cwd)
    return p.split(b'\n')


@wraps_async
def check_free_space(data_dir, file_size=0):
    """
    Check free space on dirs
    :param data_dir: string
    :param file_size: size in bytes, optional
    :return: dict, {'tmp': 200, 'data': 500, 'is_enough_space': true}
    """

    def _size(dir):
        statvfs = os.statvfs(dir)
        return statvfs.f_frsize * statvfs.f_bfree

    tmp_size = _size('/tmp')
    data_dir_size = _size(data_dir)

    if file_size:
        file_size *= 4
        enough_space = all((file_size < tmp_size, file_size < data_dir_size))
        return dict(
            tmpSpaceSize=tmp_size,
            dataSpaceSize=data_dir_size,
            enoughSpace=enough_space)

    return dict(tmpSpaceSize=tmp_size, dataSpaceSize=data_dir_size)


@wraps_async
def check_mime_type(path, mime):
    file_mime = mimetypes.MimeTypes().guess_type(path)[0]
    return file_mime == mime
