
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index,name="index"),
    path('login/',login,name="login"),
    path('register/',register,name="login"),
    path('logout/',logout,name="logout"),
    path('add-task/',add_task,name="add-task"),
    path("complete_task",complete_task,name="complete_task"),
    path('manage-tasks',manage_tasks,name="Manage Tasks"),
    path('edit-task/',edit_task,name="edit task"),
    path('delete/',delete_task,name="Delete")
]