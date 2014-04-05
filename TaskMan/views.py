from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from mainproject import settings 
from forms import *
from models import *
import utils


def index(request,template='login.html'):
	if 'status' in request.session:
		status=request.session['status']
		if status=="registered":
			return render_to_response(template,{'text':"User Aleady Registered"},context_instance=RequestContext(request))
		if status=="invalid":
			return render_to_response(template,{'text':"Invalid login credentials	"},context_instance=RequestContext(request))
		if status=="register":
			return render_to_response(template,{'text':"New User. Please Register"},context_instance=RequestContext(request))
	return render_to_response(template,context_instance=RequestContext(request))

def register(request,template='register.html'):
	return render_to_response('register.html',context_instance=RequestContext(request))


def addUser(request):
	if request.method == "POST":
		username = request.POST.get('username', '')
		userobj=User.objects.filter(pk=username)																										
		if len(userobj)==0:
			email=request.POST.get('email', '')
			password=request.POST.get('password', '')
			Userobj=User(username=username,email=email,password=password)
			Userobj.save()
			return HttpResponseRedirect('/')
		else:
			request.session['status']="registered"
			return HttpResponseRedirect('/')
	return HttpResponseNotFound('<h1>Page not found</h1>')


def taskview(request):
	if request.method == "POST":
		username = request.POST.get('username', '')
		password=request.POST.get('password', '')
		userobj=User.objects.filter(pk=username)
		if len(userobj)==1:
			if userobj[0].username==username and userobj[0].password==password:
				request.session['username']=username
				task_list=utils.getTaskList(username=username)
				return render_to_response('main.html',{'task_list':task_list,'user':username},context_instance=RequestContext(request))
			else:
				request.session['status']="invalid"
				return HttpResponseRedirect('/')
		else:
			request.session['status']="register"
			return HttpResponseRedirect('/')
			return render_to_response('login.html',{'text':"Invalid login credentials"})
	return render_to_response('login.html',{'text':"Can't login due to Security Issues"})



def addTask(request):
	form=HTMLTaskForm()
	return render_to_response('add.html',{'form':form},context_instance=RequestContext(request))


def showTask(request):
	if request.method=="POST":
		if 'add' in request.POST:
			return HttpResponseRedirect('/addTask')
		elif 'add_task' in request.POST:
			params=utils.addtasktoDB(request)
		elif 'delete' in request.POST:
			params=utils.deletetaskfromDB(request)
		elif 'update' in request.POST:
			params=utils.updateDB(request)
		elif 'sort_added' in request.POST:
			params=utils.sortByAddDate(request)
		elif 'sort_deadline' in request.POST:
			params=utils.sortByDeadline(request)
		else:
			params=showDB(request)
		return render_to_response('main.html',params,context_instance=RequestContext(request))
	return HttpResponse("Some problem")


def logout(request):
	try:
		del request.session['status']
	except KeyError:
		pass
	try:
		del request.session['username']
	except KeyError:
		pass
	return HttpResponseRedirect("/")


