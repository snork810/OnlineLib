# Generated by Django 5.1 on 2024-08-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangolib", "0002_recentlyopened"),
    ]

    operations = [
        migrations.AddField(
            model_name="ebooksmodel",
            name="cover_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="texts/covers/",
                verbose_name="Обложка книги",
            ),
        ),
    ]
