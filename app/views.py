from django.http import JsonResponse

from app.models import Student, Teacher, User


# Create your views here.
def root(request):
    fields = ["id", "username", "is_staff", "is_superuser", "role"]
    return JsonResponse(
        {
            "all_users": User.objects.count(),
            "teachers": list(Teacher.objects.values(*fields)),
            "students": list(Student.objects.values(*fields)),
        }
    )
