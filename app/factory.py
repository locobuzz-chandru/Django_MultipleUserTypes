import factory
from app.models import Student
from factory.faker import faker

FAKER = faker.Faker()


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    username = factory.Faker("text", max_nb_chars=6)
    password = factory.Faker("text", max_nb_chars=6)
