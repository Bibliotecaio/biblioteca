from django.db import models

from .managers import PublishedManager


class AbstractPublishedModel(models.Model):
    is_published = models.BooleanField(
        verbose_name='Опубликовано?', default=False)
    objects = models.Manager()
    published_objects = PublishedManager()

    class Meta:
        abstract = True
