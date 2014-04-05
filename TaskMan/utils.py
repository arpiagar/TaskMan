from models import *
from forms import *



def formatTasksTime(tasklist):
	for tasks in tasklist:
		tasks.deadline=tasks.deadline.strftime('%d %b,%Y')
		tasks.tasktime=tasks.tasktime.strftime('%d %b,%Y')
	return tasklist

def getTaskList(username):
	tasklist=Task.objects.filter(username=username)
	tasklist=formatTasksTime(tasklist)
	return tasklist


def addtasktoDB(request):
	print "Entreing add task to DB"
	form=HTMLTaskForm(request.POST)
	if form.is_valid():
		print "Valid"
		form_data= form.cleaned_data
		username=request.session['username']
		deadline_fmt= form_data['deadline'].strftime('%d %b,%Y')
		taskobj=Task(username=request.session['username'],deadline=form_data['deadline'],description=form_data['description'])
		taskobj.save()
		task_details=Task.objects.filter(pk=taskobj.taskid)
		print task_details[0].taskid,task_details[0].description
		print "object saved"
		#return HttpResponse("Valid")
		task_list=getTaskList(username=username)
		print task_list
		return {'user':username,'task_list':task_list}
	else:
		print "Invalid"
		print form.errors		
		#return HttpResponse("Invalid")
		return
	pass


def sortByDeadline(request):
	task_list=Task.objects.order_by('deadline')
	username=request.session['username']
	task_list=formatTasksTime(task_list)
	return {'user':username,'task_list':task_list}

def sortByAddDate(request):
	task_list=Task.objects.order_by('tasktime')
	username=request.session['username']
	task_list=formatTasksTime(task_list)
	return {'user':username,'task_list':task_list}

def deletetaskfromDB(request):
	id_list=request.POST.getlist('checkbox')
	for ids in id_list:
		Task.objects.filter(pk=ids).delete()
	username=request.session['username']
	task_list=getTaskList(username)
	return {'user':username,'task_list':task_list}

def updateDB(request):
	id_list=request.POST.getlist('checkbox')
	for ids in id_list:
		task_status=request.POST.get('status')
		Task.objects.filter(pk=ids).update(status=task_status)
	username=request.session['username']
	task_list=getTaskList(username)
	return {'user':username,'task_list':task_list}