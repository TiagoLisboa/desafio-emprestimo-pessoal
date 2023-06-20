from django.db import models

# Create your models here.
class ProposalField(models.Model):
    name = models.CharField(max_length=200)
    TYPE_STRING=0
    TYPE_FLOAT=1
    TYPE_INTEGER=2
    TYPE_BOOLEAN=3
    TYPE_CHOICES = [
        (TYPE_STRING, 'string'),
        (TYPE_FLOAT, 'numeric'),
        (TYPE_INTEGER, 'integer'),
        (TYPE_BOOLEAN, 'boolean'),
    ]
    field_type = models.IntegerField(choices=TYPE_CHOICES)
    is_required = models.BooleanField()

class Proposal(models.Model):
    fields = models.JSONField()
    STATUS_CHOICES = [
        ('Não Avaliada', 'Não Avaliada'),
        ('Aprovada', 'Aprovada'),
        ('Reprovada', 'Reprovada'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, default='Não Avaliada')

