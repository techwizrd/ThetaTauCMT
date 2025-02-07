# Generated by Django 2.2.12 on 2022-03-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chapters", "0010_chapter_address_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="chapter",
            name="extra_approval",
            field=models.BooleanField(
                default=False,
                help_text="Does this chapter require extra approval of automated tasks",
            ),
        ),
    ]
