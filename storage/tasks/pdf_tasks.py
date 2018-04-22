import os
import shutil
from celery import chain

from celery_app import celery_app
from utils import (
    wraps_async, get_metadata, split_pdf,
    sentry_client, Config, set_watermark, get_image_size,
    save_files_filler_batch, save_file_to_filler, update_document
)

__all__ = [
    'read_metadata',
    'split_pdf',
    'process_pdf_chain'
]

CONFIG = Config('./config/document_storage_service.yaml')()


@celery_app.task
def read_metadata(pdf_path, document_uuid, document_name):
    try:
        metadata_dict = get_metadata(pdf_path)
        return dict(
            original_document=pdf_path,
            metadata=metadata_dict,
            document_uuid=document_uuid,
            document_name=document_name,
        )
    except Exception as e:
        sentry_client(e)


@celery_app.task
def split_document(message):
    _path = message['original_document']
    _splited_path = 'splited'
    _sizes = dict(
        large=CONFIG['preview_large'],
        normal=CONFIG['preview_normal'],
        small=CONFIG['preview_small']
    )
    _format = CONFIG['preview_format']

    try:
        # TODO: Add document_name to preview images
        preview_images = split_pdf(_path, _splited_path,  _sizes, _format)
        message.update({'preview_images': preview_images})
        return message
    except Exception as e:
        sentry_client(e)


@celery_app.task
def add_watermark(message):

    if not CONFIG['watermark_add']:
        return message

    preview_images = message['preview_images']
    font = os.path.join(os.path.abspath('.'), 'fonts', CONFIG['watermark_font'])
    watermark_message = CONFIG['watermark_message']
    img_fmt = CONFIG['watermark_image_format']

    for img_path in preview_images:
        set_watermark(font, img_path, watermark_message, img_fmt)

    return message


@celery_app.task
def save_to_seaweedfs(message):
    host = CONFIG['seaweed_filler_host']
    port = CONFIG['seaweed_filler_port']

    try:
        images_list = message['preview_images']
        _dir = message['document_uuid']
        original_document = message['original_document']
        document_name = message['document_name']
        result_list = save_files_filler_batch(host, port, _dir, images_list)

        _splited = os.path.split(original_document)
        _ex = _splited[1].split('.')[1]
        document_file = '%s.%s' % (document_name, _ex)
        new_original_document = os.path.join(_splited[0], document_file)

        os.rename(original_document, new_original_document)
        save_file_to_filler(host, port, _dir, new_original_document)

        message['cover_image'] = result_list[0]
        width, height = get_image_size(images_list[0])
        message['preview_image_width'] = width
        message['preview_image_height'] = height
        message['original_document'] = document_file

        # TODO: add /tmp to conf
        shutil.rmtree(os.path.join('/tmp', _dir))
        del message['preview_images']

        return message
    except Exception as e:
        sentry_client(e)


@celery_app.task
def add_document(message):
    host = CONFIG['core_api_host']
    port = CONFIG['core_api_port']
    url = CONFIG['core_api_update_document_url']

    update_document(host, port, url, message)


@wraps_async
def process_pdf_chain(pdf_path, document_uuid, document_name):
    chain(
        read_metadata.s(pdf_path, document_uuid, document_name) |
        split_document.s() |
        add_watermark.s() |
        save_to_seaweedfs.s() |
        add_document.s()
    ).apply_async()
