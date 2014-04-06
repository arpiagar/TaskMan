import time
from django import forms
from models import User,Task
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets  


class RegisterForm(ModelForm):
	class Meta:
	    model = User
	    fields = ['username', 'email', 'password']

class TaskForm(ModelForm):
	class Meta:
	    model = Task
	    fields = ['taskid','description','deadline']
		

class HTMLTaskForm(forms.Form):
	deadline=forms.DateField(widget=widgets.AdminDateWidget,help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	description=forms.CharField()


   