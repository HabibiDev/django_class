# Generated by Django 2.1.5 on 2019-01-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20190130_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_keywords',
            field=models.TextField(blank=True),
        ),
    ]