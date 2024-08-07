# Generated by Django 5.0.6 on 2024-07-21 21:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ["-created"]},
        ),
        migrations.AddField(
            model_name="claim",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="reporter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reported_items",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="report",
            name="reporter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reports",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
