from django.contrib import admin
from django import forms

from redactor.widgets import RedactorEditor

from .models import Publication


class PublicationAdminForm(forms.ModelForm):
    class Meta:
        model = Publication
        widgets = {
           'text': RedactorEditor(),
        }
        fields = '__all__'


class PublicationAdmin(admin.ModelAdmin):
    form = PublicationAdminForm


admin.site.register(Publication)

