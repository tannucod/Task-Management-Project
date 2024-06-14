from django.shortcuts import render, redirect, HttpResponse
from .models import Task
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout 
from django.contrib.auth.models import auth
from . forms import TaskForm,RegistrationForm,LoginForm,UpdateUserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home(request):
    return render(request, 'app/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        messages.success(request,"User Registration was Successfull")
    return render(request, 'app/register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Authenticate user using the provided credentials
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                
                auth_login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})



@login_required(login_url='login')  
def dashboard(request):
    return render(request, 'app/dashboard.html')



@login_required(login_url='login')
def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('viewtask') 
    context = {'form': form}
    return render(request, 'app/createtask.html', context=context)


@login_required(login_url='login')
def view_task(request):
    current_user = request.user
    tasks = Task.objects.filter(assigned_to=current_user)
    context = {'tasks': tasks}
    return render(request, 'app/viewtask.html', context=context)



@login_required(login_url='login')
def update_task(request, pk):
   task=Task.objects.get(id=pk)
   form=TaskForm(instance=task)
   if request.method=='POST':
       form=TaskForm(request.POST,instance=task)
       if form.is_valid():
           form.save()
           return redirect('viewtask')
   context={'form':form}
   return render(request,'app/updatetask.html',context=context) 



@login_required(login_url='login')
def delete_task(request, pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
          task.delete()
          return redirect('viewtask')
          
    context={'object':task}
    return render(request,'app/deletetask.html',context=context)



@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('dashboard')  
    messages.success(request, 'Account deleted successfully!!')
    return render(request, 'app/deleteaccount.html')




def user_logout(request):
     auth.logout(request)
     messages.success(request, 'You have been logged out successfully!!')
     return redirect('app/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!!')
    return redirect('login')



#um= Admin...pw=Admin123
#um=Ramu.....pw=ramu1234     um=Samu....pw=samu12345