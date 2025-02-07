# Generated by Django 2.2.12 on 2020-05-17 17:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("scores", "0001_initial"),
        ("chapters", "0002_chapter_region"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("slug", models.SlugField(unique=True)),
                (
                    "owner",
                    models.CharField(
                        choices=[
                            ("adviser", "Adviser"),
                            ("alumni programs director", "Alumni Programs Director"),
                            ("board member", "Board Member"),
                            ("colony director", "Colony Director"),
                            ("committee chair", "Committee Chair"),
                            ("corresponding secretary", "Corresponding Secretary"),
                            ("council delegate", "Council Delegate"),
                            ("employer/ee", "Employer/Ee"),
                            ("events chair", "Events Chair"),
                            ("expansion director", "Expansion Director"),
                            ("faculty adviser", "Faculty Adviser"),
                            ("fundraising chair", "Fundraising Chair"),
                            ("grand inner guard", "Grand Inner Guard"),
                            ("grand marshal", "Grand Marshal"),
                            ("grand outer guard", "Grand Outer Guard"),
                            ("grand regent", "Grand Regent"),
                            ("grand scribe", "Grand Scribe"),
                            ("grand treasurer", "Grand Treasurer"),
                            ("grand vice regent", "Grand Vice Regent"),
                            (
                                "house corporation president",
                                "House Corporation President",
                            ),
                            (
                                "house corporation treasurer",
                                "House Corporation Treasurer",
                            ),
                            ("housing chair", "Housing Chair"),
                            ("national director", "National Director"),
                            ("national officer", "National Officer"),
                            (
                                "national operations manager",
                                "National Operations Manager",
                            ),
                            ("other appointee", "Other Appointee"),
                            ("parent", "Parent"),
                            ("pd chair", "Pd Chair"),
                            (
                                "pledge/new member educator",
                                "Pledge/New Member Educator",
                            ),
                            (
                                "professional development director",
                                "Professional Development Director",
                            ),
                            ("project chair", "Project Chair"),
                            ("recruitment chair", "Recruitment Chair"),
                            ("regent", "Regent"),
                            ("regional director", "Regional Director"),
                            ("risk management chair", "Risk Management Chair"),
                            ("rube goldberg chair", "Rube Goldberg Chair"),
                            ("scholarship chair", "Scholarship Chair"),
                            ("scribe", "Scribe"),
                            ("service chair", "Service Chair"),
                            ("service director", "Service Director"),
                            ("social/brotherhood chair", "Social/Brotherhood Chair"),
                            ("treasurer", "Treasurer"),
                            ("vice regent", "Vice Regent"),
                            (
                                "website/social media chair",
                                "Website/Social Media Chair",
                            ),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("sub", "Submission"),
                            ("form", "Forms"),
                            ("task", "Task"),
                            ("bal", "Balance"),
                        ],
                        max_length=4,
                    ),
                ),
                ("days_advance", models.PositiveIntegerField(default=90)),
                ("resource", models.CharField(blank=True, max_length=100)),
                ("description", models.CharField(max_length=1000)),
                (
                    "submission_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task",
                        to="scores.ScoreType",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="TaskDate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "school_type",
                    models.CharField(
                        choices=[
                            ("semester", "Semester"),
                            ("quarter", "Quarter"),
                            ("all", "All"),
                            ("na", "N/A"),
                        ],
                        max_length=10,
                    ),
                ),
                ("date", models.DateField(verbose_name="Due Date")),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dates",
                        to="tasks.Task",
                    ),
                ),
            ],
            options={
                "ordering": ["date"],
                "unique_together": {("task", "date", "school_type")},
            },
        ),
        migrations.CreateModel(
            name="TaskChapter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=datetime.date.today, verbose_name="Task Completed Date"
                    ),
                ),
                ("submission_id", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "chapter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="chapters.Chapter",
                    ),
                ),
                (
                    "submission_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chapters",
                        to="tasks.TaskDate",
                    ),
                ),
            ],
            options={
                "ordering": ["chapter", "-date"],
                "unique_together": {("task", "date", "chapter")},
            },
        ),
    ]
