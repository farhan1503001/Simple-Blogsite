# Generated by Django 3.2.4 on 2021-06-17 20:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0006_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
