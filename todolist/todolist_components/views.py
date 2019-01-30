from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def welcomePage(request):

    return render(request,'todolist_components/landing_page.html')

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

        return render(request, 'todolist_components/task_page.html', context=context)

@csrf_protect
def logout_link(request):
    logout(request)
    return redirect('welcomePage')
