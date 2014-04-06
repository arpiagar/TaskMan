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


def getActionList(username):
	action_list=list(Action.objects.filter(actionuser=username).order_by('actiontime'))
	action_list.reverse()	
	return action_list

def addtasktoDB(request):
	form=HTMLTaskForm(request.POST)
	username=request.session['username']
	if form.is_valid():
		form_data= form.cleaned_data		
		deadline_fmt= form_data['deadline'].strftime('%d %b,%Y')
		taskobj=Task(username=request.session['username'],deadline=form_data['deadline'],description=form_data['description'])
		taskobj.save()
		task_details=Task.objects.filter(pk=taskobj.taskid)
		task_list=getTaskList(username=username)
		action_list=getActionList(username)
		return {'user':username,'task_list':task_list,'action_list':action_list}
	else:
		return None
			


def sortByDeadline(request):
	username=request.session['username']
	task_list=Task.objects.order_by('deadline').filter(username=username)
	task_list=formatTasksTime(task_list)
	action_list=getActionList(username)
	return {'user':username,'task_list':task_list,'action_list':action_list}

def sortByAddDate(request):
	username=request.session['username']
	task_list=Task.objects.order_by('tasktime').filter(username=username)
	task_list=formatTasksTime(task_list)
	action_list=getActionList(username)
	return {'user':username,'task_list':task_list,'action_list':action_list}

def deletetaskfromDB(request):
	id_list=request.POST.getlist('checkbox')
	for ids in id_list:
		Task.objects.filter(pk=ids).delete()
	username=request.session['username']
	task_list=getTaskList(username)
	action_list=getActionList(username)
	return {'user':username,'task_list':task_list,'action_list':action_list}

def updateDB(request):
	id_list=request.POST.getlist('checkbox')
	for ids in id_list:
		task_status=request.POST.get('status')
		Task.objects.filter(pk=ids).update(status=task_status)
	username=request.session['username']
	task_list=getTaskList(username)
	action_list=getActionList(username)
	print action_list
	return {'user':username,'task_list':task_list,'action_list':action_list}