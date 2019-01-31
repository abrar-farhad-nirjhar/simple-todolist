from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import requests
from django.contrib.auth.models import User
from .models import Task
import json
# Create your views here.

def welcomePage(request):

    return render(request,'todolist_components/landing_page.html')


@csrf_protect
def task_page(request):
    data = list()
    r = requests.get(url='http://localhost:8000/tasks/')
    print("hello"*10)
    print(r.json())
    return render(request, 'todolist_components/task_page.html' )

@csrf_protect
def authenticate_user(request):

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is None:
        return redirect('welcomePage')
    else:
        login(request,user)
        context = {}
        context['user'] = user

        return redirect('task_page')

@csrf_protect
def logout_link(request):
    logout(request)
    return redirect('welcomePage')



@csrf_protect
def register_link(request):
    if request.method=='GET':
        return render(request, 'todolist_components/register_page.html')
    elif request.method=='POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        # data = {}
        # data['username'] = username
        # data['first_name'] = first_name
        # data['last_name'] = last_name
        # data['email'] = email
        # data['password'] = password

        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        
        print("THIS IS THE PASSWORD ", password)
        return redirect('welcomePage')

@csrf_protect
def add_task(request):
    t = Task()
    t.user = request.user
    t.task = request.POST['task']
    t.save()
    return redirect('task_page')
    

    




