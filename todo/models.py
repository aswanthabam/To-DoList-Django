from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
  USERNAME_FIELD = "username"
  first_name = models.CharField(max_length=200,null=False,blank=False)
  last_name = models.CharField(max_length=100,null=False,blank=False)
  email = models.EmailField(unique=True,null=False,blank=False)
  REQUIRED_FIELDS = ('first_name','last_name','email','password',) 

class Task(models.Model):
    task_id = models.AutoField(primary_key=True,unique=True)
    title = models.TextField(null=False, blank=False)
    completed = models.BooleanField(default=False)
    date_of_completion = models.DateTimeField(null=True, blank=True)
    completed_on = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return self.title

admin.site.register(Task)
admin.site.register(CustomUser)