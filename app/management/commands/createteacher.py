from getpass import getpass

from django.core.management.base import BaseCommand

from app.models import Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--email", type=str)

    def handle(self, *args, **options):
        payload = {
            "username": options["username"],
            "email": options["email"],
            "password": getpass("Password: "),
        }
        obj = Teacher.objects.create_teacher(**payload)

        self.stdout.write(
            self.style.SUCCESS(
                "Teacher %(name)s added successfully added"
                % {"name": obj.username}
            )
        )
