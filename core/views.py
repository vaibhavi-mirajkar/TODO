from django.shortcuts import render,redirect
from .models import TODO
# Create your views here.

def todo_home(request):
    if request.method=="POST":
        title=request.POST.get("title")
        if title:
            TODO.objects.create(title=title) 
            return redirect('todo_home')
        
    todos=TODO.objects.all() 
    return render(request,'core/todo_home.html',{'todos':todos})

def complete_todo(request,todo_id):
    todo =TODO.objects.get(srno=todo_id)
    todo.completed = True
    todo.save()
    return redirect("todo_home")

def delete_todo(request,todo_id):
    TODO.objects.get(srno=todo_id).delete()
    return redirect("todo_home")

def todo_edit(request,todo_id):
    todo = TODO.objects.get(srno=todo_id)

    if request.method == "POST":
        new_title = request.POST.get("title")
        if new_title:
            todo.title = new_title
            todo.save()
            return redirect("todo_home")
    return render(request, 'core/todo_edit.html', {'todo': todo})