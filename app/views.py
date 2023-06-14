import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import (Student, Teacher, User)
from .permissions import create_groups
from django.conf import settings
from utils.utils import JWT, verify_superuser


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
        model.objects.create_staff(**data)
        return JsonResponse({"message": "created"}, status=201)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


@csrf_exempt
def add_teacher(request):
    return fun(request, Teacher)


@csrf_exempt
def add_student(request):
    return fun(request, Student)


@csrf_exempt
def login(request):
    try:
        data = json.loads(request.body)
        user = authenticate(username=data.get("username"), password=data.get("password"))
        token = JWT().encode({"user_id": user.id})
        return JsonResponse({"token": token, "message": 'Login Successful'}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


@csrf_exempt
@verify_superuser
def create_group(request):
    try:
        for group in settings.GROUP_PERMISSIONS.keys():
            create_groups(group_name=group)
        return JsonResponse({"message": "created"}, status=201)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)
