# Generated by Django 2.1.5 on 2019-01-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('pub_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
