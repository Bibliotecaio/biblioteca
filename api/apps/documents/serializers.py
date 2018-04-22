from rest_framework import serializers

from .models import (Document, DocumentType, Keyword, Author,
                     Language, Subject, TimePeriod)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'code')


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ('id', 'name')


class TimePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimePeriod
        fields = ('id', 'begin_year', 'end_year', 'period')


class DocumentSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=False, required=False)
    document_type = DocumentTypeSerializer(many=False, required=False)
    authors = AuthorSerializer(many=True, required=False)
    keywords = KeywordSerializer(many=True, required=False)
    subject = SubjectSerializer(many=False, required=False)
    time_period = TimePeriodSerializer(many=False, required=False)

    class Meta:
        model = Document
        fields = (
            'id',
            'document_uuid',
            'document_file_original',
            'title',
            'physical_place',
            'cover_image',
            'preview_image_width',
            'preview_image_height',
            'creation_date',
            'last_update_date',
            'description',
            'document_number',
            'document_source_date',
            'file_type',
            'page_count',
            'physical_description',
            'producer',
            'subject',
            'toc',
            'authors',
            'document_type',
            'keywords',
            'language',
            'time_period',
            'is_document_processed',
            'download_link',
        )


class DocumentListSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(many=False, required=False)
    document_type = DocumentTypeSerializer(many=False, required=False)
    authors = AuthorSerializer(many=True, required=False)
    keywords = KeywordSerializer(many=True, required=False)
    subject = SubjectSerializer(many=False, required=False)
    time_period = TimePeriodSerializer(many=False, required=False)

    class Meta:
        model = Document
        fields = (
            'id',
            'title',
            'physical_place',
            'cover_image',
            'creation_date',
            'description',
            'document_number',
            'document_source_date',
            'page_count',
            'physical_description',
            'subject',
            'authors',
            'document_type',
            'keywords',
            'language',
            'time_period',
            'download_link'
        )


class FiltersInitialSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    authors = AuthorSerializer(many=True, read_only=True)