"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .viewsets import *
from .views import *
router = SimpleRouter()

router.register('tasks', TaskViewset)
router.register('users', UserViewset)



urlpatterns = [
    path('welcomePage', welcomePage, name="welcomePage"),
    path('authenticate_user', authenticate_user, name="authenticate"),
    path('logout', logout_link, name="logout"),
    path('register', register_link, name='register'),
    path('add_task', add_task, name='add_task'),
    path('task_page', task_page, name='task_page')
    
    
]+router.urls
