# Generated by Django 2.0.2 on 2020-02-09 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200208_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
    ]
