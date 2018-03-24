from django.db import models
from django.contrib.postgres.fields import JSONField

from core.models import AbstractPublishedModel

from .managers import RandomManager, PublishedByDateManager

__all__ = [
    'Language',
    'DocumentType',
    'Document',
    'Keyword',
    'Author',
]


"""

3) Описание - краткое описание (например издательство, ISBN, кол-во страниц,...)
5) Дата выпуска (год или век, если неизвестно)
7) Место хранение - место+номер хранение (для рукописей и старопечатных книг)
9) Ссылка на скачивание
Издатель

"""


class TimePeriod(models.Model):
    begin_year = models.DateField(
        verbose_name='Год начала', blank=True, null=True)
    end_year = models.DateField(
        verbose_name='Год окончания', blank=True, null=True)

    class Meta:
        unique_together = (('begin_year', 'end_year'),)
        verbose_name = 'Временной период'
        verbose_name_plural = 'Временные периоды'

    def __str__(self):
        return self.period

    @property
    def period(self):
        return '%s–%s' % (
            self.begin_year.strftime('%Y'), self.end_year.strftime('%Y'))


class Language(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    code = models.CharField(verbose_name='Код', max_length=10)

    class Meta:
        verbose_name = 'Язык документа'
        verbose_name_plural = 'Языки документов'

    def __str__(self):
        return self.name


class DocumentType(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Типы документов'

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(verbose_name='Тема', max_length=255)

    class Meta:
        verbose_name = 'Тема документа'
        verbose_name_plural = 'Темы документа'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)

    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключеые слова'

    def __str__(self):
        return self.name


PHYSICAL_PLACE = (
    ('archive', 'Архив'),
    ('library', 'Библиотека'),
)


class Document(AbstractPublishedModel):
    display_on_home = models.BooleanField(
        verbose_name='Показывать на главной?', default=True)
    title = models.CharField(
        verbose_name='Название документа', max_length=500, blank=True)
    document_number = models.CharField(
        verbose_name='Номер документа в физическом хранилище',
        max_length=255, blank=True)
    physical_place = models.CharField(
        choices=PHYSICAL_PLACE, default='ARCHIVE', max_length=100,
        verbose_name='Место размещения')
    language = models.ForeignKey(
        'Language', verbose_name='Язык документа', null=True, blank=True)
    time_period = models.ForeignKey(
        'TimePeriod', verbose_name='Временной период', null=True, blank=True)
    document_type = models.ForeignKey(
        'DocumentType', verbose_name='Тип документа', null=True, blank=True)
    subject = models.ForeignKey(
        'Subject', verbose_name='Тема документа', null=True, blank=True)
    description = models.TextField(verbose_name='Описание',  blank=True)
    file_type = models.CharField(
        verbose_name='Тип файла', max_length=10, blank=True)
    producer = models.CharField(
        verbose_name='Издатель', max_length=255, blank=True)
    page_count = models.PositiveIntegerField(
        verbose_name='Количество страниц', default=0)
    cover_image = models.CharField(
        verbose_name='Ссылка на обложку документа', max_length=255, blank=True)
    preview_image_width = models.PositiveIntegerField(
        verbose_name='Ширина изоображения для просмотра', default=0)
    preview_image_height = models.PositiveIntegerField(
        verbose_name='Высота изоображения для просмотра', default=0)
    physical_description = models.TextField(
        verbose_name='Физическое описание документа', blank=True)
    document_source_date = models.DateField(
        verbose_name='Дата создания оригинала документа', blank=True, null=True)
    creation_date = models.DateTimeField(
        verbose_name='Дата создания документа в системе', auto_now_add=True)
    last_update_date = models.DateTimeField(
        verbose_name='Дата обновления документа в системе', auto_now=True)
    toc = JSONField(verbose_name='Оглавление документа',  blank=True, null=True)
    authors = models.ManyToManyField(
        'Author', verbose_name='Авторы документа', blank=True)
    keywords = models.ManyToManyField(
        'Keyword', verbose_name='Ключевые слова', blank=True)
    is_document_file_processed = models.BooleanField(default=False)
    is_document_processed = models.BooleanField(
        default=False, verbose_name='Обработан ли документ?',)
    document_uuid = models.CharField(
        max_length=255, null=True, blank=True, db_index=True,
        verbose_name='UUID документа')
    document_file_original = models.CharField(
        max_length=500, null=True, blank=True, verbose_name='Файл документа')
    objects = models.Manager()
    random_objects = RandomManager()
    published_by_date_objects = PublishedByDateManager()

    def __str__(self):
        return '%d: %s' % (self.id, self.title)

    class Meta:
        ordering = ['title']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def to_json(self):
        return dict(
            id='82753-lefler-thesis',
            title="Lefler Thesis",
            pages=129,
            description="A Master's Thesis on the phenomenon of \"LOLSPEAK\" and its origin in image macros.",
            source=None,
            created_at="Tue, 10 Jan 2012 20:20:36 +0000",
            updated_at="Fri, 09 Feb 2018 16:40:27 +0000",
            canonical_url="http://localhost:8000",
            language="eng",
            file_hash=None,
            contributor="Ted Han",
            contributor_slug="2258-ted-han",
            contributor_documents_url="http://localhost:8000/public/search/Account:2258-ted-han",
            contributor_organization="DocumentCloud",
            contributor_organization_slug="dcloud",
            contributor_organization_documents_url="http://localhost:8000",
            display_language="eng",
            resources={
                "pdf": "https://assets.documentcloud.org/documents/282753/lefler-thesis.pdf",
                "text": "https://assets.documentcloud.org/documents/282753/lefler-thesis.txt",
                "thumbnail": "https://assets.documentcloud.org/documents/282753/pages/lefler-thesis-p1-thumbnail.gif",
                "search": "https://www.documentcloud.org/documents/282753/search.json?q={query}",
                "print_annotations": "https://www.documentcloud.org/notes/print?docs[]=282753",
                "translations_url": "https://www.documentcloud.org/translations/{realm}/{language}",
                "page": {
                    "image": "https://assets.documentcloud.org/documents/282753/pages/lefler-thesis-p{page}-{size}.gif",
                    "text": "https://www.documentcloud.org/documents/282753/pages/lefler-thesis-p{page}.txt"
                },
                "published_url": "http://localhost:8000"
            },
            sections=[],
            data={},
            annotations=[]
        )
