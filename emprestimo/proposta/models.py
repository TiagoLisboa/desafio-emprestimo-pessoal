from django.db import models

# Create your models here.
class ProposalField(models.Model):
    name = models.CharField(max_length=200)
    field_type = models.IntegerField(choices=[
        (0, 'string'),
        (1, 'numeric'),
        (2, 'boolean'),
    ])
    is_required = models.BooleanField()

class Proposal(models.Model):
    fields = models.JSONField()
    status = models.CharField(choices=[
        ('Não Avaliada', 'Não Avaliada'),
        ('Aprovada', 'Aprovada'),
        ('Reprovada', 'Reprovada'),
    ], default='Não Avaliada')

