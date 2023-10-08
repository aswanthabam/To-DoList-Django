from django.contrib.auth.models import Permission
from todo.models import Task
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

task_edit_permission = Permission.objects.create(
    codename='can_edit_task',
    name='Can Edit Task',
    content_type=ContentType.objects.get_for_model(Task)
)

my_group = Group.objects.create(name='Normal')

my_group.permissions.add(task_edit_permission)
