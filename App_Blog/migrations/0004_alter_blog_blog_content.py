# Generated by Django 3.2 on 2021-09-09 09:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0003_auto_20210826_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='What is on your mind?'),
        ),
    ]
