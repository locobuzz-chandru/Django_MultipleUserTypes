import json
from django.http import JsonResponse
from app.models import Student, Teacher


def root(request):
    students = Student.objects.values_list("username", flat=True)
    teachers = Teacher.objects.values_list("username", flat=True)
    data = {
        "Students": [student for student in students],
        "Teachers": [teacher for teacher in teachers]
    }
    return JsonResponse(data)


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
