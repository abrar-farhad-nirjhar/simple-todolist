from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.





class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=255, null=False, blank=False)
