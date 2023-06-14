from django.contrib.auth.models import (Group, Permission)
from django.conf import settings


def _get_codenames(group_name: str):
    group = settings.GROUP_PERMISSIONS.get(group_name)
    return [f"{action}_{model}" for model, actions in group.items() for action in actions]


def get_or_create_group(group_name: str):
    group, is_created = Group.objects.get_or_create(name=group_name)
    if is_created:
        codenames: list = _get_codenames(group_name=group_name)
        permissions = [Permission.objects.get(codename=codename) for codename in codenames]
        group.permissions.set(list(permissions))
        group.save()
    return group
