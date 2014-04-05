import time
from django import forms
from models import User,Task
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets  
"""class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100,required=true)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    emmail = forms.EmailField()"""

class RegisterForm(ModelForm):
	class Meta:
	    model = User
	    fields = ['username', 'email', 'password']

class TaskForm(ModelForm):
	class Meta:
	    model = Task
	    fields = ['taskid','description','deadline']
	def __init__(self, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['deadline'].widget = widgets.AdminDateWidget()
		#self.fields['mytime'].widget = widgets.AdminTimeWidget()
		#self.fields['mydatetime'].widget = widgets.AdminSplitDateTime()

STATUS_CHOICES = ('Incomplete','Complete')


class HTMLTaskForm(forms.Form):
	#taskid=forms.Autofield(primary_key=True)
	#status = forms.CharField(max_length=10,widget=forms.Select(choices=STATUS_CHOICES))
	deadline=forms.DateField(widget=widgets.AdminDateWidget,help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
	#deadline=forms.DateField(widget=SelectDateWidget('%d %b, %Y'))
	#tasktime=forms.DateField(initial= time.strftime('%d %b,%Y'))
	description=forms.CharField()
	#x`username=forms.CharField(max_length=100)

def set_password(self, raw_password):
	import random
	algo = 'sha1'
	salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
	hsh = get_hexdigest(algo, salt, raw_password)
	self.password = '%s$%s$%s' % (algo, salt, hsh)
   