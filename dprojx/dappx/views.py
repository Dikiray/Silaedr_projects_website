from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from dappx.forms import UserForm,ProjectForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import ProjectInfo
# Create your views here.
def index(request):
    print(2)
    projects = ProjectInfo.objects.all()
    return render(request,'dappx/index.html', {"projects":projects, })
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    print(3)
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    print(1)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'registered':registered})
def user_login(request):
    print(4)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})

def create_new_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(data=request.POST)
        if project_form.is_valid():
            project = project_form.save()
            project.project_picture = request.FILES['project_picture']
            project.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        project_form = ProjectForm()
        return render(request,'dappx/new_project.html',{'project_form':project_form,})
