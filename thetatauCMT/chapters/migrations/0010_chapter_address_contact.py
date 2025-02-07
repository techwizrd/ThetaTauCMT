# Generated by Django 2.2.12 on 2021-11-07 20:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chapters", "0009_chapter_health_safety_surcharge"),
    ]

    operations = [
        migrations.AddField(
            model_name="chapter",
            name="address_contact",
            field=models.CharField(
                default="Not Set",
                help_text="Name of person to contact at address for deliveries",
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="chapter",
            name="address_phone_number",
            field=models.CharField(
                default=1111111111,
                help_text="Phone number to contact at address for deliveries.Format: 9999999999 no spaces, dashes, etc.",
                max_length=17,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
            preserve_default=False,
        ),
    ]
