# Generated by Django 5.1 on 2024-08-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_nomoderatedbooksmodel_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nomoderatedbooksmodel",
            name="user",
            field=models.CharField(max_length=80, verbose_name="Введите свой никнэйм"),
        ),
    ]
