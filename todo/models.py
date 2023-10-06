from django.db import models

class UserModel(models.Model):
  name = models.TextField(null=False)
  email = models.TextField(null=False,unique=True)
  password = models.TextField(null=False)
  def __str__(self):
    return "f{_id}-name"