# Generated by Django 4.2.1 on 2023-05-07 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_homepage_banner_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="banner_title",
            field=models.CharField(default="Welcome to my homepage!", max_length=100),
        ),
    ]
