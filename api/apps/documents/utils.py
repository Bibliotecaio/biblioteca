import os
import uuid

import requests
from pytils import translit
from django.conf import settings

from core.utils import sentry_client
from .models import (Language, Keyword, Author, DocumentType,
                     Subject, TimePeriod)


def get_storage_info(url):

    try:
        response = requests.get(url=url)
        if response.status_code != 200:
            raise requests.ConnectionError
        return response.content
    except requests.ConnectionError as e:
        sentry_client(e)
        return False


def add_document(url, files):
    files = {'upload_file': open(files, 'rb')}
    try:
        response = requests.post(url, files=files)
        if response.status_code not in [200, 415, 507]:
            raise requests.ConnectionError
        return dict(status=response.status_code, msg=response.json())
    except requests.ConnectionError as e:
        sentry_client(e)
        return False


def get_search_filter_initial():

    _models = Language, Keyword, Author, DocumentType, Subject

    def _time_period(p):
        return dict(
            id=p.id,
            period=p.period,
            begin_year=p.begin_year,
            end_year=p.end_year,
        )

    def _to_cc(s):
        return s[0].lower() + s[1:]

    result_dict = {
        '%ss' % _to_cc(c.__name__): list(c.objects.values()) for c in _models}
    result_dict.update(
        {
            'timePeriods': map(_time_period, TimePeriod.objects.all()),
            'alphabetChars': [
                {'char': char} for char in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']
         }
    )
    return result_dict


def save_document_file(file_obj, document_name) -> tuple:
    f_name = file_obj.name.split('.')
    _uuid = str(uuid.uuid4())
    name = '%s.%s' % (_uuid, f_name[1])
    f = '/tmp/%s' % name

    with open(f, 'wb') as temp:
        for chunk in file_obj.chunks():
            temp.write(chunk)

    url = '%s?name=%s' % (settings.ADD_DOCUMENT_URL, translit.slugify(document_name))
    response = add_document(url=url, files=f)
    os.remove(f)
    return response, name
