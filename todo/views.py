from django.shortcuts import render
"""
Home router consit of home, register, login
"""
def index(request):
  return render(request,"home.django")
def login(request):
  return render(request,"login.html")
def register(request):
  return render(request,"register.html")