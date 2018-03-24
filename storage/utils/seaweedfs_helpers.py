import requests
from utils import sentry_client


__all__ = [
    'save_file',
    'save_files_batch',
    'save_file_to_filler',
    'save_files_filler_batch'
]


def save_file(host, port, file_path):
    """
    Save file to Seaweed FS

    :param host: str, master host
    :param port: int, master post
    :param file_path: str, path to file
    :return: str, file fid
    """
    files = {'upload_file': open(file_path, 'rb')}
    url = 'http://%s:%d/submit' % (host, port)
    try:
        response = requests.post(url, files=files)
        return response.json()['fid']
    except Exception as e:
        sentry_client(e)
        raise e


def save_file_to_filler(host, port, directory, file_path):
    """
    Save file to Seaweed FS

    :param host: str, master host
    :param port: int, master port
    :param directory: filler unique dir
    :param file_path: str, path to file
    :return: str, file fid
    """
    files = {'upload_file': open(file_path, 'rb')}
    url = 'http://%s:%s/%s/' % (host, port, directory)
    try:
        response = requests.post(url, files=files)
        return response.json()['fid']
    except Exception as e:
        sentry_client(e)
        raise e


def save_files_batch(host, port, files_list):

    def _save_file(path):
        return save_file(host, port, path)

    return list(map(_save_file, files_list))


def save_files_filler_batch(host, port, directory, files_list):

    def _save_file(path):
        return save_file_to_filler(host, port, directory, path)

    return list(map(_save_file, files_list))
