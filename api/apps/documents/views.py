import os
import pytils

from django.http import JsonResponse, HttpResponse
from django.conf import settings

from rest_framework.response import Response
from rest_framework import viewsets, permissions, views, parsers, mixins
from rest_framework.generics import get_object_or_404

from .utils import (get_storage_info, save_document_file,
                    get_search_filter_initial)
from .models import (Language, Keyword, Author, DocumentType,
                     Document)
from .serializers import (
    LanguageSerializer, KeywordSerializer, AuthorSerializer,
    DocumentTypeSerializer, DocumentSerializer, DocumentListSerializer)

from .search import search_document_by_title, join_queries


class StorageInfoView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):

        url = settings.STORAGE_INFO_URL
        storage_info = get_storage_info(url)

        if storage_info:
            return Response(storage_info)
        return Response(status=504)


class SearchFilterInitialView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request):
        return Response(data=get_search_filter_initial())


class DocumentViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,):
    serializer_class = DocumentSerializer
    queryset = Document.published_by_date_objects.all()

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        filtered_queryset = join_queries(request.query_params, queryset)

        query = request.query_params.get('q', None)
        if query:
            filtered_queryset = search_document_by_title(query)

        page = self.paginate_queryset(filtered_queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class DocumentRandomViewSet(DocumentViewSet):
    serializer_class = DocumentListSerializer
    queryset = Document.random_objects.all()


class DocumentUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = 'document_uuid'

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {lookup_url_kwarg: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)
        return obj


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects
    serializer_class = AuthorSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects
    serializer_class = KeywordSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    model = Language
    queryset = model.objects
    serializer_class = LanguageSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.queryset

        obj = self.model.objects.filter()

        if 'document_pk' in self.kwargs:
            document_pk = self.kwargs['document_pk']
            obj = queryset.filter(document__pk=document_pk).first()

        data = self.serializer_class(obj).data
        return Response(data)


class DocumentTypeViewSet(viewsets.ModelViewSet):
    model = DocumentType
    queryset = model.objects
    serializer_class = DocumentTypeSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.queryset

        obj = self.model.objects.filter()

        if 'document_pk' in self.kwargs:
            document_pk = self.kwargs['document_pk']
            obj = queryset.filter(document__pk=document_pk).first()

        data = self.serializer_class(obj).data
        return Response(data)


class DocumentViewerView(views.APIView):

    def get(self, request, document_id, *args, **kwargs):
        obj = get_object_or_404(Document.published_by_date_objects.all(), id=document_id)

        return JsonResponse(data=obj.to_json())