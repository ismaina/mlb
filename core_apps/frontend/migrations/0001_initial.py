# Generated by Django 4.2.1 on 2023-05-25 14:27

import core_apps.common.utils
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('message', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=core_apps.common.utils.upload_image_path)),
                ('supported', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'contacts',
            },
        ),
    ]
