from django.http import JsonResponse

from app.models import Student, Teacher


# Create your views here.
def root(request):
    s = Teacher.objects.all()
    print(s)
    return JsonResponse({})