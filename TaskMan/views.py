from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse,HttpResponseNotFound
from mainproject import settings 

def index(request,template='login.html'):
	return render_to_response(template)

def register(request,template='register.html'):
	return render_to_response('register.html')

def verifyUser(request):
	pass

@csrf_protect
def addUser(request):
	return HttpResponse(request.method)
	c = {}
	c.update(csrf(request))
	if request.method == "POST":
		user=request.username
		password=request.password
		return render_to_response(user,c)
	return HttpResponseNotFound('<h1>Page not found</h1>',c)
