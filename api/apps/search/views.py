from rest_framework.response import Response
from rest_framework import views


from .utils import searcher


class SearchView(views.APIView):

    def get(self, request, format=None):
        query_str = request.query_params.get('q', None)

        if not query_str:
            return Response(status=400, data=dict(message='Неверный запрос'))
        return searcher(query_str, request)
