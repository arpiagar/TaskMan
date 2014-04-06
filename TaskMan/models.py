from django.db import models
import time
# Create your models here.

import datetime


class User(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.username



class Task(models.Model):
	taskid=models.AutoField(primary_key=True)
	username=models.CharField(max_length=100)
	tasktime=models.DateTimeField(default=datetime.datetime.now())
	description=models.CharField(max_length=300)
	deadline=models.DateTimeField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	status=models.CharField(max_length=10,default="Incompleted")
	

class Action(models.Model):
	actionid=models.AutoField(primary_key=True)
	actiontime=models.DateTimeField(default=datetime.datetime.now())
	actiontype=models.CharField(max_length=10)
	actionuser=models.CharField(max_length=100)
	actiondescription=models.CharField(max_length=150)



