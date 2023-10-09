
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index,name="index"),
    path('login/',login,name="login"),
    path('register/',register,name="login"),
    path('logout/',logout,name="logout"),
    path('add-task/',add_task,name="add-task")
]