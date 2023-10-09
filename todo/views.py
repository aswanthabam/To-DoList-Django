from django.http import HttpResponseRedirect as redirect
from django.shortcuts import render
from .forms import UserForm, TaskForm
from .models import CustomUser, Task
from django.contrib.auth import authenticate, login as loguser, logout as loguserout
from datetime import datetime
from django.db.models import Q

"""
Index Route
"""
def index(request):
  if request.user.is_authenticated:
    if request.method == "GET":
      state = request.GET.get("s")
      ctx = {}
      if state == "e":
        # expired 
        tasks = Task.objects.filter(user=request.user,completed=False,date_of_completion__lt= datetime.now())
        ctx["texpired"] = True
        pass
      elif state == "c":
        # completed
        tasks = Task.objects.filter(user=request.user,completed=True)
        ctx["tcompleted"] = True
      else:
        tasks = Task.objects.filter(Q(date_of_completion__gt=datetime.now()) | Q(date_of_completion__isnull=True),user=request.user,completed=False)
        ctx["ttask"] = True
      ctx["tasks"] = tasks
      return render(request,"home.html",ctx)
    request.session['toast'] = "Invalid Route!"
    return redirect("/")
  return render(request,"get-started.html")
  

"""
Login Route
"""
def login(request):
  if request.user.is_authenticated:
    request.session['toast'] = "You are logged in already, Try <a href='/logout'>Logout</a>"
    return redirect("/")
  if(request.method == "POST"):
    username = request.POST["username"]
    password = request.POST["password"]
    try:user = CustomUser.objects.get(username=username)
    except:user = None
    print(user)
    if user is not None and user.password == password:
      # user = authenticate(request, user)
      if user is not None:
        loguser(request, user)
        request.session['toast'] = "Welcome back "+user.first_name+"!"
        print("Success")
        return redirect("/")
      else:
        request.session["toast"] = "An error occured!"
        return redirect("/login")
    else:
      request.session["toast"] = "Invalid username or password!"
      return redirect("/login")
  return render(request,"login.html")
"""
Register Route
"""
def register(request):
  if request.user.is_authenticated:
    request.session['toast'] = "You are logged in already, Try <a href='/logout'>Logout</a>"
    return redirect("/")
  if(request.method == "POST"):
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = request.POST["username"]
      loguser(request,user)
      request.session["toast"] = "Successfully logged in as @"+username
      return redirect("/")
  else:
    form = UserForm()
  return render(request,"register.html",{"form":form})
"""
Logout Route
"""
def logout(request):
  if not request.user.is_authenticated:
    request.session['toast'] = "You are not logged in!"
    return redirect("/")
  loguserout(request)
  request.session['toast'] = "Successfully logged out!"
  return redirect("/")
"""
Add Task Route
"""
def add_task(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      title = request.POST.get('title')
      date_co = request.POST.get('date_of_completion')
      if title == None:
        request.session['toast'] = "Invalid request!"
        return redirect("/")
      try:
        task = Task(title=title,date_of_completion=None if date_co == "" else date_co,user=request.user)
        task.save()
      except Exception as e:
        print(e)
        request.session['toast'] = "An error occured"
        return redirect("/")
      request.session['toast'] = "Successfully added task!"
      return redirect("/")
  else:
    request.session['toast'] = "You are not logged in!"
    return redirect("/login")
  return redirect("/")
 
"""
Route Complete task
"""
def complete_task(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      task_id = request.POST.get("task_id")
      completed = request.POST.get("completed")
      if task_id == None or task_id == "":
        request.session["toast"] = "Error : Invalid Task"
        return redirect("/")
      task = Task.objects.get(task_id=task_id,user=request.user)
      if task == None:
        request.session["toast"] = "Error : Invalid Task, User Mismatch"
        return redirect("/")
      if completed == None or completed == "" or completed == "1":
        completed = True
      else:completed = False 
      task.completed = completed
      task.completed_on = datetime.now()
      task.save()
      request.session["toast"] = "Marked as completed!" if completed else "Marked as non completed"
      return redirect("/")
    return redirect("/")
  else:
    request.session["toast"] = "Please login to continue"
    return redirect("/login")