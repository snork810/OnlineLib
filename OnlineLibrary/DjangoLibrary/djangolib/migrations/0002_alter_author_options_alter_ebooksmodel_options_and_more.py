# Generated by Django 5.1 on 2024-08-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangolib", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"verbose_name": "Автор", "verbose_name_plural": "Авторы"},
        ),
        migrations.AlterModelOptions(
            name="ebooksmodel",
            options={
                "verbose_name": "Электронная книга",
                "verbose_name_plural": "Электронные книги",
            },
        ),
        migrations.AlterField(
            model_name="ebooksmodel",
            name="category",
            field=models.CharField(max_length=80, verbose_name="Категория"),
        ),
        migrations.AlterField(
            model_name="ebooksmodel",
            name="pages",
            field=models.CharField(max_length=80, verbose_name="Количество страниц"),
        ),
        migrations.AlterField(
            model_name="ebooksmodel",
            name="pdf",
            field=models.FileField(upload_to="Texts/", verbose_name="Загрузите файл"),
        ),
        migrations.AlterField(
            model_name="ebooksmodel",
            name="summary",
            field=models.TextField(max_length=10000, verbose_name="Аннотация"),
        ),
        migrations.AlterField(
            model_name="ebooksmodel",
            name="title",
            field=models.CharField(max_length=80, verbose_name="Название"),
        ),
    ]
