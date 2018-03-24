from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

from rest_framework.authtoken.models import Token

ADMIN = 'admin'
EDITOR = 'editor'
SITE_USER = 'site_user'

ROLES = (
    (ADMIN, 'Администратор'),
    (EDITOR, 'Редактор'),
    (SITE_USER, 'Обычный пользователь'),
)


class UserManager(BaseUserManager):

    def _build_user(self, email, password, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None):
        return self._build_user(email=email, password=password)

    def create_superuser(self, email, password):
        return self._build_user(email=email, password=password,
                                is_superuser=True, is_active=True)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(
        verbose_name='Имя', max_length=30, blank=True)
    last_name = models.CharField(
        verbose_name='Фамилия', max_length=30, blank=True)
    patronymic = models.CharField(
        verbose_name='Отчество', max_length=30, blank=True)
    role = models.CharField(
        verbose_name='Роль', choices=ROLES, default=SITE_USER, max_length=100)
    is_superuser = models.BooleanField(
        verbose_name='Администратор', default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'

    def __str__(self):
        return self.short_name

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def short_name(self):
        return self.get_short_name()

    def has_module_perms(self, app_label):
        if self.is_active and self.is_superuser:
            return True

    def has_perm(self, perm_name):
        if not self.is_active:
            return False

        if self.is_superuser:
            return True

        try:
            app_label, model, code_name = perm_name.split('.')
        except ValueError:
            return False

        return self.permissions.filter(
            content_type__app_label=app_label,
            content_type__model=model,
            code_name=code_name
        ).exists()

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def role_name(self):
        roles_dict = dict(ROLES)
        return roles_dict[self.role]

    @staticmethod
    def post_save(sender, instance, created, *args, **kwargs):
        if created:
            template = get_template('users/mail/letter.html')

            context = Context({
                'name': instance.full_name,
                'login': instance.short_name,
                'password': instance.password
            })

            to, from_email = instance.email, settings.DEFAULT_FROM_EMAIL
            content = template.render(context)
            msg = EmailMultiAlternatives(
                '[Учетные данные]', content, from_email, [to]
            )
            msg.attach_alternative(content, "text/html")
            msg.send()


post_save.connect(sender=User, receiver=User.post_save)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

