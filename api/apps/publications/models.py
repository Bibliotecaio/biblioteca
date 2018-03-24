from django.db import models
from django.db.models import signals
from django.dispatch import receiver

from redactor.fields import RedactorField
from chakert import Typograph

from core.models import AbstractPublishedModel


class Publication(AbstractPublishedModel):
    headline = models.CharField(verbose_name='Заголовок', max_length=500)
    text = RedactorField(verbose_name='Текст публикации')
    date = models.DateField(verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-date']

    def __str__(self):
        return '%s %s' % (self.headline, self.date.strftime('%Y-%m-%d'))


@receiver(signals.pre_save, sender=Publication)
def typofgraphy(sender, instance=None, created=False, **kwargs):
    #instance.headline = Typograph.typograph_text(instance.headline, 'ru')
    #instance.text = Typograph.typograph_text(instance.text, 'ru')
    pass
