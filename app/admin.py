from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Student, Teacher, User


class UserAdmin(admin.ModelAdmin):

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(id=request.user.id)


admin.site.register(User)
admin.site.register(Student, UserAdmin)
admin.site.register(Teacher, UserAdmin)

# Student.objects.create_student(username='s5', password='s5')
# python manage.py shell
# from app.models import Student, Teacher
# Teacher.objects.create_teacher(username='t5', password='t5')
