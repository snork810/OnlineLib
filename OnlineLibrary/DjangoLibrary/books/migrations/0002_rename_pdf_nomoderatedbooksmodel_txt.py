# Generated by Django 5.1 on 2024-08-18 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="nomoderatedbooksmodel",
            old_name="pdf",
            new_name="txt",
        ),
    ]
