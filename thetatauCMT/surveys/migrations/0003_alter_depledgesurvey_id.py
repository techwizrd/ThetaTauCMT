# Generated by Django 3.2.15 on 2022-08-21 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0002_survey"),
    ]

    operations = [
        migrations.AlterField(
            model_name="depledgesurvey",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
