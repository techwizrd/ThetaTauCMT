# Generated by Django 2.2.12 on 2021-08-21 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chapters", "0006_auto_20210424_1306"),
    ]

    operations = [
        migrations.AddField(
            model_name="chapter",
            name="house",
            field=models.BooleanField(
                blank=True,
                default=False,
                null=True,
                verbose_name="Does your chapter have a house?",
            ),
        ),
    ]
