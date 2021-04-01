from django.db import models

# Create your models here.
class Task (models.Model):
    userName = models.CharField(max_length=8, default='')
    email = models.CharField(max_length=40, default='')
    textTask = models.CharField(max_length=250, default='')
    statusTask = models.IntegerField(null=False, default=0)