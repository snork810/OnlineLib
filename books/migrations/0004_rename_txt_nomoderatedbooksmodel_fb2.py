# Generated by Django 5.1 on 2024-08-21 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_alter_nomoderatedbooksmodel_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="nomoderatedbooksmodel",
            old_name="txt",
            new_name="fb2",
        ),
    ]
