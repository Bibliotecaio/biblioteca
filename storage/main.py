import asyncio
import logging

from aiohttp import web

from routers import setup_routes


def init(_config):
    loop = asyncio.get_event_loop()

    # setup application and extensions
    app = web.Application(loop=loop)

    setup_routes(app)

    return app


def main(_config):
    # init logging
    logging.basicConfig(level=logging.DEBUG)

    app = init(_config)
    web.run_app(app, host=_config['host'], port=_config['port'])


if __name__ == '__main__':
    import sys
    from utils import Config

    info = 'Usage: main.py ./config/document_storage_service.yaml'

    try:
        config = Config(sys.argv[1])()
        main(config)

    except (TypeError, ValueError, IndexError):
        sys.exit(info)
    if len(sys.argv) < 2:
        sys.exit(info)
