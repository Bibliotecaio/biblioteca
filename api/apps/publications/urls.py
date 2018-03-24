from django.conf.urls import include, url
from rest_framework_nested import routers

from .views import PublicationViewSet


router = routers.SimpleRouter()
router.register(r'publications', PublicationViewSet, base_name='publications')


urlpatterns = [
    url(r'^', include(router.urls)),
]

