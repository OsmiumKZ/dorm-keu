# Generated by Django 2.2.2 on 2019-06-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='educational_form',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Форма обучения'),
        ),
    ]
