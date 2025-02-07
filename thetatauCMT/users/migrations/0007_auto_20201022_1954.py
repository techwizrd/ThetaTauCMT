# Generated by Django 2.2.12 on 2020-10-23 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20201003_0813"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userstatuschange",
            name="status",
            field=models.CharField(
                choices=[
                    ("alumni", "alumni"),
                    ("alumnipend", "alumni pending"),
                    ("active", "active"),
                    ("activepend", "active pending"),
                    ("pnm", "prospective"),
                    ("away", "away"),
                    ("depledge", "depledge"),
                    ("advisor", "advisor"),
                    ("resigned", "resigned"),
                ],
                max_length=10,
            ),
        ),
    ]
