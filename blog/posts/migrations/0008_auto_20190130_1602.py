# Generated by Django 2.1.5 on 2019-01-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20190130_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_keywords',
            field=models.TextField(null=True),
        ),
    ]
