from django.db import models


class RandomManager(models.Manager):
    def get_queryset(self):
        return super(RandomManager, self).get_queryset().filter(
            is_published=True, display_on_home=True).order_by('?')


class PublishedByDateManager(models.Manager):
    def get_queryset(self):
        return super(PublishedByDateManager, self).get_queryset().filter(
            is_published=True).order_by('-creation_date')
