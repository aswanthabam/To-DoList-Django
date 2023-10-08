from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
# Create your views here.
@require_POST
def login(request):
  print(request.POST)
  return render(request,"login.html")
@require_POST
def register(request):
  post = request.POST
  username = post.get('username')
  fname = post.get('fname')
  sname = post.get('sname')
  email = post.get('email')
  password = post.get('password')
  ctx = {}
  if username and password and fname and sname and email:
    print(username,password,email,fname,sname)
    pass
  else:
    ctx = {
      "error":"Please fill all fields",
      "username":False if username else True,
      "fname":False if fname else True,
      "sname":False if sname else True,
      "email":False if email else True,
      "password":False if password else True,
      "post":post

    }
    return render(request,"register.html",ctx)