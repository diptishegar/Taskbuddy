from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import tasklist
from todolist.models import d
from todolist.form import taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



@login_required
def todolist(request):
    if request.method == "POST":
        form = taskform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            if d == None:
                messages.success(request, "Enter a Task!!")
            else:
                messages.success(request, "New Task Added!!!")
        return redirect('todolist')
    else:
       all_tasks = tasklist.objects.filter(owner=request.user)
       paginator = Paginator(all_tasks, 7)
       page = request.GET.get("page")
       all_tasks = paginator.get_page(page)
       return render(request, 'todolist.html', {'all_tasks' : all_tasks})
   
@login_required   
def delete_task(request, task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.owner==request.user:
        task.delete()
    else:
        messages.error(request, ("Access not allowed"))
    return redirect('todolist')

@login_required
def  edit_task(request, task_id):
    if request.method == "POST":
        task = tasklist.objects.get(pk=task_id)
        form = taskform(request.POST or None, instance=task)
        form.save()
        if form.is_valid():
            form.save()
        messages.success(request, "Task Edited!!!")
        return redirect('todolist')
    else:
       task_dip = tasklist.objects.get(pk=task_id)
       return render(request, 'edit.html', {'task_dip' : task_dip})
   
def index(request):
    context = {
       'index_text':"Welcome to Index page"
       }
    return render(request, 'index.html', context)

def contact(request):
    context = {
       'contact_text':"Welcome to Contact page"
       }
    return render(request, 'contact.html', context)


def about(request):
    context = {
       'about_text':"Welcome to About page"
       }
    return render(request, 'about.html', context)

@login_required   
def complete_task(request, task_id):
    task = tasklist.objects.get(pk=task_id)
    if task.owner==request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Access not allowed"))
        
    return redirect('todolist')
@login_required
def pending_task(request, task_id):
    task = tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')
