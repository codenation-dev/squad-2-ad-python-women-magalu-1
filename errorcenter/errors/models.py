import re

from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.conf import settings
from django.core.validators import validate_ipv4_address


LEVEL_CHOICES = [
    ('critical', 'Critical'),
    ('debug', 'Debug'),
    ('error', 'Error'),
    ('warning', 'Warning'),
    ('information', 'Info'),
]


ENVIRONMENT_CHOICES = [
    ('development', 'Dev'),
    ('homologation', 'Homologação'),
    ('production', 'Produção'),
]


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff,
                     is_superuser, **extra_fields):
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email, is_staff=is_staff, is_active=True,
            is_superuser=is_superuser, last_login=now,
            date_joined=now, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password,
                                 False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password,
                                 True, True, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(('Primeiro Nome'), max_length=30, null=True, blank=True)
    last_name = models.CharField(('Último Nome'), max_length=30, blank=True)
    email = models.EmailField(('E-mail'), max_length=255, unique=True)
    date_joined = models.DateTimeField(('Criado em'), default=timezone.now)

    is_staff = models.BooleanField(
        ('Acesso ao Admin'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        ('Ativo'),
        default=True,
        help_text=('Designates whether this user should be treated as active.'
                   + 'Unselect this instead of deleting accounts.'))

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class Error(models.Model):
    title = models.CharField('Título', max_length=254)
    description = models.TextField('Descrição', max_length=500)
    level = models.CharField('Tipo', max_length=20, choices=LEVEL_CHOICES)
    environment = models.CharField(
        'Ambiente',
        max_length=20,
        choices=ENVIRONMENT_CHOICES
    )
    address = models.GenericIPAddressField(
        'Endereço IP',
        validators=[validate_ipv4_address]
    )
    created_at = models.DateTimeField('Data de Criação', auto_now_add=True)
    events = models.IntegerField('Eventos')
    filed = models.BooleanField('Arquivado', default=False)
    excluded = models.BooleanField('Excluído', default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.deletion.DO_NOTHING,
        related_name='errors'
    )

    def __str__(self):
        return f'[{self.level}] {self.title}'
