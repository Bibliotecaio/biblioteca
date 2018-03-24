import re
import operator
from functools import reduce

from django.db.models import Q

from .models import Document


def _split_q(q):
    q_list = re.split(r'\s+', q)
    if q_list[0]:
        return q_list
    return []


def search_document_by_title(query):
    query_list = _split_q(query)
    return Document.published_objects.filter(
        reduce(operator.or_, (Q(title__icontains=q) for q in query_list)))


def _construct_q(attr, q) -> dict:
    return {'%s__pk__in' % attr: _split_q(q)}


def join_queries(query_params, queryset):

    document_id = query_params.get('documentId', '')
    if document_id:
        return queryset.filter(pk=document_id)

    physical_place = _split_q(query_params.get('physicalPlace', ''))
    limit = query_params.get('limit', '')

    query_dict = dict(
        authors=query_params.get('authors', ''),
        time_period=query_params.get('timePeriods', ''),
        document_type=query_params.get('documentTypes', ''),
        language=query_params.get('languages', ''),
        subject=query_params.get('subjects', ''),
        keywords=query_params.get('keywords', '')
    )

    chars = _split_q(query_params.get('alphabetChars', ''))
    q_list = []

    q_list.extend([Q(**_construct_q(k, v)) for k, v in query_dict.items() if v])
    if physical_place:
        q_list.append(Q(physical_place__in=physical_place))
    if chars:
        q_list.append(reduce(operator.or_, (Q(title__iregex=r"^%s{1}" % q) for q in chars)))
    if q_list:
        filtered_qs = queryset.filter(reduce(operator.and_, q_list)).distinct()
        if limit:
            return filtered_qs[:int(limit[0])]
        return filtered_qs
    if limit:
        return queryset[:int(limit[0])]
    return queryset


