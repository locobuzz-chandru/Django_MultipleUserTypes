import json
from django.http import JsonResponse
from app.models import (Student, Teacher, User)


def root(request):
    fields = ["id", "username", "is_staff", "is_superuser", "role"]
    return JsonResponse(
        {
            "all_users": User.objects.count(),
            "teachers": list(Teacher.objects.values(*fields)),
            "students": list(Student.objects.values(*fields)),
        }
    )


def fun(request, model):
    try:
        data = json.loads(request.body)
        if model == Teacher:
            Teacher.objects.create_teacher(**data)
        elif model == Student:
            Student.objects.create_student(**data)
        return JsonResponse({"message": "created"}, status=201)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


def add_teacher(request):
    return fun(request, Teacher)


def add_student(request):
    return fun(request, Student)
