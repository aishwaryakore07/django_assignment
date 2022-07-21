from django.shortcuts import render, redirect
from .models import Task
from .forms import *

# Create your views here.
def todoList(request):
    # read todo list item
    items = Task.objects.all()
    form = TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    items = Task.objects.all()
    form = TaskForm()
    return render(request, 'todo/index.html',{'items':items, 'form':form})

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'todo/update.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)
	item.delete()
	return redirect('/')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)
# def addItem(request):
#     if request.method=='POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             form.save()
#         # return redirect('/')
#     items = Items.objects.all()
#     return render(request, 'todo/index.html',{'items':items, 'form':form})
    



# def deleteItem(request, pk):
#     item_to_delete = Task.objects.get(id=pk)
#     if request.method=='POST':
#         item_to_delete.delete()

#     items = Items.objects.all()
#     return render(request,'todo/indexhtml',{'items':items})