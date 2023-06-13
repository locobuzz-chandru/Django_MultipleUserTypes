from django.contrib.auth.models import (Group, Permission)


def add_group_and_permissions(actions: list, group_name: str):
    permissions = [Permission.objects.get(codename=codename) for codename in actions]
    group, _ = Group.objects.get_or_create(name=group_name)
    group.permissions.set(list(permissions))
    group.save()
    return group


def create_teacher_group(group_name):
    codenames = ["add_student", "change_student", "view_student", "view_teacher"]
    return add_group_and_permissions(actions=codenames, group_name=group_name)


def create_student_group(group_name):
    codenames = ["view_student"]
    return add_group_and_permissions(actions=codenames, group_name=group_name)
