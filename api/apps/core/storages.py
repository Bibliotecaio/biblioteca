from __future__ import absolute_import

import errno
import os

from django.core.files import File, locks
from django.utils._os import safe_join
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible

from .utils import SeaweedFSClient, setting


@deconstructible
class SeaweedfsStorage(Storage):
    """
    Seaweedfs Storage class for Django pluggable storage system.
    """

    def __init__(self, seaweedfs_host=None,
                 seaweedfs_port=None,
                 seaweedfs_volume_host=None,
                 seaweedfs_volume_port=None):
        host = seaweedfs_host or setting('SEAWEEDFS_HOST')
        port = seaweedfs_port or setting('SEAWEEDFS_PORT')
        self.seaweedfs_volumne_host = seaweedfs_volume_host or setting(
            'SEAWEEDFS_VOLUME_HOST')
        self.seaweedfs_volume_port = seaweedfs_volume_port or setting(
            'SEAWEEDFS_VOLUME_PORT')

        if host is None:
            raise ImproperlyConfigured("You must configure a seaweedfs "
                                       "host auth at"
                                       "'settings.SEAWEEDFS_HOST'.")
        self.client = SeaweedFSClient(host, port)

    def url(self, name):
        return '%s:%d/%s' % (
            self.seaweedfs_volumne_host, self.seaweedfs_volume_port, name)

    def exists(self, name):
        return False

    def path(self, name):
        return safe_join('/tmp', name)

    def _save(self, name, content):

        full_path = self.path(name)
        # Create any intermediate directories that do not exist.
        # Note that there is a race between os.path.exists and os.makedirs:
        # if os.makedirs fails with EEXIST, the directory was created
        # concurrently, and we can continue normally. Refs #16082.
        directory = os.path.dirname(full_path)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        if not os.path.isdir(directory):
            raise IOError("%s exists and is not a directory." % directory)

        # This fun binary flag incantation makes os.open throw an
        # OSError if the file already exists before we open it.
        flags = (os.O_WRONLY | os.O_CREAT | os.O_EXCL |
                 getattr(os, 'O_BINARY', 0))
        # The current umask value is masked out by os.open!
        fd = os.open(full_path, flags, 0o666)
        _file = None
        try:
            locks.lock(fd, locks.LOCK_EX)
            for chunk in content.chunks():
                if _file is None:
                    mode = 'wb' if isinstance(chunk, bytes) else 'wt'
                    _file = os.fdopen(fd, mode)
                _file.write(chunk)
        finally:
            locks.unlock(fd)
            if _file is not None:
                _file.close()
            else:
                os.close(fd)
        file_name = self.client.put(self.path(name))
        os.unlink(full_path)
        return file_name
