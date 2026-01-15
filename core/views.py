from django.shortcuts import render,redirect
from .models import TODO
from django.contrib import messages
from django.contrib.auth.models import User
from . import views
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if not username or not password:
            messages.error(request,"All fields are required")
            return redirect("signup")
        
        if password != confirm_password:
            messages.error(request, "passwords do not match")
            return redirect("signup")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken,Please try another one")
            return redirect("signup")
        
        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect("login")
    
    return render(request,"core/signup.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Both fields are required")
            return redirect("login")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todo_home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    
    return render(request, "core/login.html")
        

