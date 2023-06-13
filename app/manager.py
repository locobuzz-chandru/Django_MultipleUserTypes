from django.contrib.auth.models import (Group, UserManager)


class MyManager(UserManager):

    @staticmethod
    def _add_user_to_group(group_name, user_obj):
        group = Group.objects.get(name=group_name)
        user_obj.groups.add(group)
        user_obj.save()
        return user_obj

    def create(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)


class StudentManager(MyManager):

    def create_student(self, username, email=None, password=None, **extra_fields):
        return super()._add_user_to_group("student",
                                          self.create(username, email, password, **extra_fields))


class TeacherManager(MyManager):

    def create_teacher(self, username, email=None, password=None, **extra_fields):
        return super()._add_user_to_group("staff",
                                          self.create(username, email, password, **extra_fields))
