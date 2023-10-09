from django.db import models
from django.forms import ModelForm
from .models import CustomUser, Task
from django import forms
# Create your models here.

class UserForm(ModelForm):
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
  class Meta:
    model = CustomUser
    fields = ["first_name","last_name","email","username","password"]
    widgets = {
        'password':forms.PasswordInput()
    }

class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta:
        model = Task
        fields = ['title','date_of_completion']
        widgets = {
          'date_of_completion':forms.DateTimeInput()
        }