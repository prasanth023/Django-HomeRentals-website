# Generated by Django 4.1.5 on 2023-04-11 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0008_temporary_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporary',
            name='agreement_date',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='temporary',
            name='end_date',
            field=models.CharField(default='', max_length=20),
        ),
    ]
