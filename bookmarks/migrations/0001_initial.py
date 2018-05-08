# Generated by Django 2.0.5 on 2018-05-08 23:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField(unique=True, verbose_name='URL')),
                ('name', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
    ]
