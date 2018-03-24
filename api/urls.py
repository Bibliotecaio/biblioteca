from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from rest_framework.authtoken import views

from api import settings

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE


urlpatterns = [
    url(r'^api/', include('users.urls')),
    url(r'^api/', include('documents.urls',  namespace='documents')),
    url(r'^api/', include('publications.urls',  namespace='publications')),
    url(r'^api/', include('search.urls',  namespace='search')),

    url(r'^api/admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^viewer/$', TemplateView.as_view(template_name='document-viewer/viewer.html')),
    url(r'^redactor/', include('redactor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.extend(staticfiles_urlpatterns())
