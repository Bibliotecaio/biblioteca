from rest_framework import viewsets

from core.permissions import RetrieveListPermission

from .models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.published_objects.all()
    serializer_class = PublicationSerializer
    permission_classes = (RetrieveListPermission,)
