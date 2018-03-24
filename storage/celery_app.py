from celery import Celery
from utils import Config

config = Config('./config/document_storage_service.yaml')()
AMQP_URL = 'amqp://%s:%s@localhost:5672//' % (config['amqp_user'],
                                              config['amqp_password'])


celery_app = Celery(
    'document_storage',
    backend='rpc://',
    broker=AMQP_URL,
    include=['tasks']
)


celery_app.conf.update(
    CELERY_ENABLE_UTC=True,
    CELERY_ALWAYS_EAGER=False,
    CELERY_ROUTES={
        'tasks.pdf_tasks.read_metadata': {'queue': 'read_metadata'},
        'tasks.pdf_tasks.split_document': {'queue': 'split_document'},
        'tasks.pdf_tasks.add_watermark': {'queue': 'add_watermark'},
        'tasks.pdf_tasks.save_to_seaweedfs': {'queue': 'save_to_seaweedfs'},
        'tasks.pdf_tasks.add_document': {'queue': 'add_document'},
    }
)
