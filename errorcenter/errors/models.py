from django.db import models
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
    # Usuário (chave estrangeira) ou Token do Usuário
    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.deletion.DO_NOTHING,
    #     related_name='errors'
    # )
    # token = models.CharField('Token do Usuário', max_length=254)

    def __str__(self):
        return f'[{self.level}] {self.title}'
