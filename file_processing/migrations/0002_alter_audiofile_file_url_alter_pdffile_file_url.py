# Generated by Django 4.2.7 on 2023-12-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_processing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='file_url',
            field=models.URLField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='pdffile',
            name='file_url',
            field=models.URLField(max_length=1024, null=True),
        ),
    ]
