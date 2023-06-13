from getpass import getpass

from django.core.management.base import BaseCommand

from app.models import Student


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--email", type=str)

    def handle(self, *args, **options):
        payload = {
            "username": options["username"],
            "email": options["email"],
            "password": getpass("Password: "),
        }
        obj = Student.objects.create_student(**payload)

        self.stdout.write(
            self.style.SUCCESS(
                "Student %(name)s added successfully added"
                % {"name": obj.username}
            )
        )
