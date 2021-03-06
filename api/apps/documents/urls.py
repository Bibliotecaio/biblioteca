from django.conf.urls import include, url
from rest_framework_nested import routers

#from .routers import ListRouter
from .views import (
    LanguageViewSet,
    KeywordViewSet,
    AuthorViewSet,
    DocumentViewSet,
    DocumentTypeViewSet,
    StorageInfoView,
    DocumentUpdateViewSet,
    SearchFilterInitialView,
    DocumentViewerView
)


router = routers.SimpleRouter()
router.register(r'languages', LanguageViewSet, base_name='languages')
router.register(r'keywords', KeywordViewSet, base_name='keywords')

router.register(
    r'document-types', DocumentTypeViewSet, base_name='document-types')
router.register(r'authors', AuthorViewSet, base_name='authors')
router.register(r'documents', DocumentViewSet, base_name='documents')


urlpatterns = [
    url(r'', include(router.urls)),
    url(r'document-update/(?P<document_uuid>[\w-]+)/$', DocumentUpdateViewSet.as_view({'put': 'update', 'get': 'retrieve'}), name='document_update'),
    url(r'document-viewer/(?P<document_id>[\d-]+)/$', DocumentViewerView.as_view(), name='document_viewer'),
    url(r'storage-info/$', StorageInfoView.as_view(), name='storage_info'),
    url(r'initial-filters/$', SearchFilterInitialView.as_view({'get': 'list'}), name='initial_filters'),
]

