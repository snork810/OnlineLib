# Generated by Django 5.1 on 2024-08-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0004_rename_txt_nomoderatedbooksmodel_fb2"),
    ]

    operations = [
        migrations.AddField(
            model_name="nomoderatedbooksmodel",
            name="cover_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="texts/nomoderated/covers/",
                verbose_name="Обложка книги",
            ),
        ),
    ]
