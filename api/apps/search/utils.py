import re
import operator
import itertools
from functools import reduce
from html.parser import HTMLParser
from collections import OrderedDict

from django.db.models import Q
from django.conf import settings
from rest_framework.response import Response

from documents.models import Document
from .paginators import Pagination


class HTMLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = HTMLStripper()
    s.feed(html)
    return s.get_data()


def _split_q(q):
    q_list = re.split(r'\s+', q)
    if q_list[0]:
        return q_list
    return []


def _search_documents(query_list):
    by_title = reduce(
        operator.or_, (Q(title__icontains=q) for q in query_list))
    by_description = reduce(
        operator.or_, (Q(description__icontains=q) for q in query_list))

    queries = Q()
    queries.add(by_title, Q.OR)
    queries.add(by_description, Q.OR)

    return Document.published_objects.filter(queries)


def _search_item(item_dict, section):
    title = ''
    snippet = ''

    if section == 'books':
        title = item_dict['title']
        snippet = item_dict['description']
    elif section == 'publications':
        title = item_dict['headline']
        snippet = item_dict['text']

    return dict(
        id=item_dict['id'],
        title=title,
        snippet=strip_tags(snippet[:200]),
        section=section
    )


def _search(query_str):
    query_list = _split_q(query_str)

    document_list = list(
        _search_documents(query_list).values('id', 'title', 'description'))

    document_results = [_search_item(i, 'books') for i in document_list]
    results_list = document_results

    count = 1
    for item in results_list:
        item['order'] = count
        count += 1
    return results_list


def _grouper(n, iterable, fillvalue=None):
    """
    _grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    """
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)


def _filter_none(item):
    return list(list(filter(None, item)))


def searcher(query_str, request):
    page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
    results_list = _search(query_str)
    total_count = len(results_list)

    page = int(request.query_params.get('page', 1))

    paginator = Pagination(page, page_size, total_count, request)
    data = [_filter_none(i) for i in _grouper(page_size, results_list)]

    if page > paginator.pages and data:
        return Response(status=404, data=dict(message='Страницы нет'))

    return Response(OrderedDict([
        ('count', total_count),
        ('total_pages', paginator.pages if paginator.pages else 1),
        ('current', paginator.page),
        ('next', paginator.get_next_link()),
        ('previous', paginator.get_previous_link()),
        ('query', query_str),
        ('results', data[page - 1] if data else [])
    ]))
