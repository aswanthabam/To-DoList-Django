from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

class Task(models.Model):
    task_id = models.AutoField(primary_key=True,unique=True)
    title = models.TextField(null=False, blank=False)
    completed = models.BooleanField(default=False)
    date_of_completion = models.DateField(null=True, blank=True)
    completed_on = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return self.title

admin.site.register(Task)