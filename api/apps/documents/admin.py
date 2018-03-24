from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

from .models import (Language, Keyword, Document,
                     DocumentType, Author, TimePeriod, Subject)
from .utils import save_document_file
from .widgets import ReadonlyInput


class DocumentAdminForm(forms.ModelForm):
    document_file = forms.FileField(required=True, label='Файл документа')

    def __init__(self, *args, **kwargs):
        super(DocumentAdminForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if all([instance, instance.pk, instance.is_document_file_processed]):
            self.fields['document_file'].widget = ReadonlyInput('Файл загружен')
            self.fields['document_file'].required = False

    class Meta:
        model = Document
        fields = '__all__'
        exclude = ('is_document_file_processed', )

    def clean_document_file(self):
        file_obj = self.cleaned_data.get('document_file', None)
        document_name = self.cleaned_data.get('title')

        if file_obj:
            response, name = save_document_file(file_obj, document_name)
            file_obj.name = name
            if not response:
                raise ValidationError('Хранилище недоступно')
            if response['status'] == 415:
                raise ValidationError('Тип файла не поддерживется')
            if response['status'] != 200:
                raise ValidationError(response['msg']['message'])
        return file_obj


class DocumentAdmin(admin.ModelAdmin):
    form = DocumentAdminForm

    def _document_number(self, instance):
        return '%s/%s' % (instance.document_number, instance.id)

    _document_number.short_description = 'Номер'

    list_display = (
        'title', '_document_number', 'physical_place',
        'is_document_processed', 'is_published', 'display_on_home'
    )

    def get_readonly_fields(self, request, obj=None):
        return [
            'document_uuid', 'is_document_processed',
            'file_type', 'page_count', 'cover_image',
            'preview_image_width', 'preview_image_height',
            'document_file_original',
        ]

    def save_model(self, request, obj, form, change):
        if form.is_valid() and not obj.is_document_file_processed:
            _uuid = form.cleaned_data["document_file"].name.split('.')[0]
            obj.document_uuid = _uuid
            obj.is_document_file_processed = True
        obj.save()


admin.site.register(Language)
admin.site.register(Subject)
admin.site.register(Keyword)
admin.site.register(DocumentType)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Author)
admin.site.register(TimePeriod)
