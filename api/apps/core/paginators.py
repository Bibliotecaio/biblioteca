from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPagination(pagination.PageNumberPagination):
    def get_total_pages(self):

        additional_page = 0
        if (self.page.paginator.count % self.page_size) > 0:
            additional_page = 1

        full_pages = self.page.paginator.count // self.page_size

        return full_pages + additional_page

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('total_pages', self.get_total_pages()),
            ('current', self.page.number),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
