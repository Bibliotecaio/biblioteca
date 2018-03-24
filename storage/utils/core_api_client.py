import requests
from utils import sentry_client

__all__ = [
    'update_document',
]


def update_document(host, port, url, message_dict):
    """
    Save document to core api
    """

    document_uuid = message_dict['document_uuid']
    url = 'http://%s:%d/%s/%s/' % (host, port, url, document_uuid)
    headers = {'content-type': 'application/json; charset=utf-8'}

    try:
        message = {
            'is_document_processed': True,
            'coverImage': message_dict['cover_image'],
            'previewImageWidth': message_dict['preview_image_width'],
            'previewImageHeight': message_dict['preview_image_height'],
            'fileType': 'pdf',
            'pageCount': message_dict['metadata'].get('number_of_pages', 0),
            'toc': message_dict['metadata'].get('toc', []),
            'document_file_original': message_dict['original_document'],
        }
        response = requests.put(url, json=message, headers=headers,)
        if response.status_code != 200:
            sentry_client(
                'API Error: CODE %d, CONTENT: %s' % (
                    response.status_code, str(response.json()))
            )
    except Exception as e:
        sentry_client(e)
        raise e
