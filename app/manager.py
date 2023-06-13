from django.contrib.auth.models import Group, UserManager
from app.permissions import create_teacher_group, create_student_group


class StudentManager(UserManager):
    @staticmethod
    def _add_user_to_group(obj):
        group = create_student_group(group_name="student")
        obj.groups.add(group)
        obj.save()
        return obj

    def create_student(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        user = self._create_user(username, email, password, **extra_fields)
        return self._add_user_to_group(user)

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=self.model.Role.STUDENT)


class TeacherManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=self.model.Role.TEACHER)

    @staticmethod
    def _add_user_to_group(obj):
        group = create_teacher_group(group_name="teacher")
        obj.groups.add(group)
        obj.save()
        return obj

    def create_teacher(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        user = self._create_user(username, email, password, **extra_fields)
        return self._add_user_to_group(user)
