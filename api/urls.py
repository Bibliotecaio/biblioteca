from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from api import settings

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE


urlpatterns = [
    url('api/', include('users.urls')),
    url('api/', include('documents.urls')),
    url('api/', include('search.urls')),
    url('manage/', admin.site.urls),
    url('', TemplateView.as_view(template_name='index.html')),
    url('viewer/', TemplateView.as_view(template_name='document-viewer/viewer.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.extend(staticfiles_urlpatterns())
