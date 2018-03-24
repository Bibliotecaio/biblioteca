import os
import aiofiles
from aiohttp import web

from tasks import process_pdf_chain
from utils import check_free_space, check_mime_type, Config

CONFIG = Config('./config/document_storage_service.yaml')()


async def get_storage_info(request):
    storage_info = await check_free_space(CONFIG['seaweed_data_dir'])
    return web.json_response(data=storage_info)


async def add_document(request):
    reader = await request.multipart()
    _file = await reader.next()
    filename = _file.filename
    content_length = reader.headers.get("Content-Length", 0)
    storage_state = await check_free_space(
        CONFIG['seaweed_data_dir'], int(content_length))

    if not storage_state['enoughSpace']:
        return web.json_response(
            status=507, data=dict(message='Недостаточно места в хранилище'))

    document_uuid = os.path.splitext(filename)[0]
    path = os.path.join('/tmp', document_uuid, filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    async with aiofiles.open(path, 'wb') as f:
        while True:
            chunk = await _file.read_chunk()
            if not chunk:
                break
            await f.write(chunk)

    pdf = await check_mime_type(path, 'application/pdf')
    if pdf:
        document_name = request.query.get('name', document_uuid)
        await process_pdf_chain(path, document_uuid, document_name)

        return web.json_response(
            data=dict(message='Файл %s добавлен в обработку' % filename)
        )

    return web.json_response(
        status=415,
        data=dict(message='Тип файла %s не поддерживается' % filename)
    )
