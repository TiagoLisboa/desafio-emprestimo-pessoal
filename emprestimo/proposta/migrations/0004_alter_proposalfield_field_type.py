# Generated by Django 4.2.2 on 2023-06-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposta', '0003_proposal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalfield',
            name='field_type',
            field=models.IntegerField(choices=[(0, 'string'), (1, 'numeric'), (2, 'integer'), (3, 'boolean')]),
        ),
    ]