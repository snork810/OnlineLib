# Generated by Django 5.1 on 2024-08-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nomoderatedbooksmodel",
            name="txt",
            field=models.FileField(
                upload_to="texts/nomoderated/", verbose_name="Загрузите файл"
            ),
        ),
    ]
