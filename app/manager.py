from django.contrib.auth.models import UserManager as BaseUserManager
from django.contrib.auth.models import Group


def _add_user_to_group(obj, group_name):
    group = Group.objects.get(name=group_name)
    obj.groups.add(group)
    obj.save()
    return obj


class UserManager(BaseUserManager):
    def create_staff(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        user = self._create_user(username, email, password, **extra_fields)
        return _add_user_to_group(user, user.role.lower())


class StudentManager(UserManager):

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=self.model.Role.STUDENT)


class TeacherManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=self.model.Role.TEACHER)
