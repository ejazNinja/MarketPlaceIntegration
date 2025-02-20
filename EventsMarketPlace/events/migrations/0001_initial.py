# Generated by Django 5.0.6 on 2024-06-14 09:37

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("base_event_id", models.CharField(max_length=10)),
                ("event_id", models.CharField(max_length=10)),
                ("title", models.CharField(max_length=255)),
                ("start_date_time", models.DateField()),
                ("end_date_time", models.DateField()),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
    ]
