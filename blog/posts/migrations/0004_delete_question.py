# Generated by Django 2.1.5 on 2019-01-23 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
