# Generated by Django 2.2.6 on 2019-12-11 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20191210_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artpage',
            name='artist',
        ),
    ]
