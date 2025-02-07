"""
Notes:
    To test run command
        docker-compose -f local.yml run --rm django python manage.py officer_update_reminder_email
"""
# Includes
import datetime
from django.core.management import BaseCommand
from django.core.mail import send_mail
from users.notifications import OfficerUpdateReminder
from chapters.models import Chapter


class Command(BaseCommand):
    # Show this when the user types help
    help = "Send email to eboard positions to remind to update"

    def add_arguments(self, parser):
        parser.add_argument("-override", action="store_true")
        parser.add_argument("-chapter", nargs="+", type=str)
        parser.add_argument("-rdonly", action="store_true")

    # A command must define handle()
    def handle(self, *args, **options):
        today = datetime.date.today().strftime("%d")
        chapters_only = options.get("chapter", None)
        if chapters_only is not None:
            chapters = Chapter.objects.filter(slug__in=chapters_only)
        else:
            chapters = Chapter.objects.exclude(active=False)
        for chapter in chapters:
            if not chapter.active:
                continue
            print(chapter)
            emails, officers_to_update = chapter.get_about_expired_coucil()
            if officers_to_update:
                print(f"Sending message to: {chapter}\n")
                result = OfficerUpdateReminder(
                    chapter, emails, officers_to_update
                ).send()
                print("    ", result)
            else:
                print(f"{chapter} does not need to update CMT\n")
