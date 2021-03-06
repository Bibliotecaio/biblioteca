import requests

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def sentry_client(error):
    print(error)


def setting(name, default=None, strict=False):
    """
    Helper function to get a Django setting by name. If setting doesn't exists
    it can return a default or raise an error if in strict mode.
    :param name: Name of setting
    :type name: str
    :param default: Value if setting is unfound
    :param strict: Define if return default value or raise an error
    :type strict: bool
    :returns: Setting's value
    :raises: django.core.exceptions.ImproperlyConfigured if setting is unfound
             and strict mode
    """
    if strict and not hasattr(settings, name):
        msg = "You must provide settings.%s" % name
        raise ImproperlyConfigured(msg)
    return getattr(settings, name, default)


class SeaweedFSClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def put(self, file_path) -> str:
        """
        Save file to Seaweed FS

        :param file_path: str, path to file
        :return: str, file fid
        """
        files = {'upload_file': open(file_path, 'rb')}
        url = 'http://%s:%d/submit' % (self.host, self.port)

        response = requests.post(url, files=files)
        return response.json()['fid']

