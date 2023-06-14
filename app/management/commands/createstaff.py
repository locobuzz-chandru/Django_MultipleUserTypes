from getpass import getpass
from django.core.management.base import BaseCommand
from app.models import Student, Teacher
from utils.validate_email import validate_email
from utils.exception_classes import InvalidEmailError, PasswordMissMatchError


class Command(BaseCommand):
    help = "Creates staff user"

    def handle(self, *args, **options):
        staff_type = input("Staff type [teacher/student]: ")
        payload = {
            "username": input("username: "),
            "email": input("email: "),
            "password": getpass("Password: "),
            "password1": getpass("Confirm Password: "),
        }
        models = {
            "student": Student,
            "teacher": Teacher
        }
        model = models.get(staff_type)

        if model is None:
            raise KeyError("Entered Incorrect Staff Type")
        if not validate_email(payload.get("email")):
            raise InvalidEmailError("Entered Invalid Email")
        if payload.get("password") != payload.get("password1"):
            raise PasswordMissMatchError("Passwords are not matching")

        payload.pop("password1")

        obj = model.objects.create_staff(**payload)

        self.stdout.write(
            self.style.SUCCESS(
                "Staff %(name)s added successfully"
                % {"name": obj.username}
            )
        )
