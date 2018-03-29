from math import ceil
from rest_framework.utils.urls import remove_query_param, replace_query_param


class Pagination(object):
    """
    Custom pagination for client side
    """

    def __init__(self, page, per_page, total_count, request):
        self.request = request
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def _has_prev(self):
        return self.page > 1

    @property
    def _has_next(self):
        return self.page < self.pages

    def get_next_link(self):
        if not self._has_next:
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page + 1
        return replace_query_param(url, 'page', page_number)

    def get_previous_link(self):
        if not self._has_prev:
            return None
        url = self.request.build_absolute_uri()
        page_number = self.page
        if page_number == 1:
            return remove_query_param(url, 'page')
        page_number = self.page - 1
        return replace_query_param(url, 'page', page_number)
