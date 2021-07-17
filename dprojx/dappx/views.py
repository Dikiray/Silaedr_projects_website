from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from dappx.forms import UserForm,ProjectForm,SortForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import ProjectInfo
# Create your views here.
def index(request):
    direction = ""
    if request.method == 'POST':
        direction = dict(request.POST)["direction"][0]
    if "Все" in direction:
        direction = ""
    projects = ProjectInfo.objects.all
    return render(request,'dappx/index.html', {"projects":projects,"direction": direction})
#user part
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors)
            return HttpResponse("Форма была не полностью заполнена или такой пользователь уже существует")
    else:
        user_form = UserForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'registered':registered})
def user_login(request):
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
            return HttpResponse("Неправильный пароль или логин")
    else:
        return render(request, 'dappx/login.html', {})
#Project part
def create_new_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            project_form = ProjectForm(data=request.POST)
            if project_form.is_valid():
                project = project_form.save()
                project.project_acount = request.user
                project.project_picture = request.FILES['project_picture']
                project.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Форма была не полностью заполнена")
        else:
            project_form = ProjectForm()
            return render(request,'dappx/new_project.html',{'project_form':project_form,})
    else:
        return HttpResponse("Вы не вошли в акаунт")

def project(request, name):
    project = ProjectInfo.objects.filter(project_name=name).first()
    if request.method == "POST":
        if request.user.is_authenticated and request.user.is_staff:
            project.project_state = request.POST['project_state']
            project.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request,'dappx/project.html', {'project':project})

def change_project(request, name):
    dict_project = ProjectInfo.objects.filter(project_name=name).values()[0]
    project = ProjectInfo.objects.filter(project_name=name).first()
    if request.user.is_authenticated and project.project_acount == request.user:
        if request.method == 'POST':
            project_form = ProjectForm(data=request.POST)
            if project_form.is_valid():
                project.project_creators = project_form['project_creators'].value()
                project.project_name = project_form['project_name'].value()
                project.project_root = project_form['project_root'].value()
                project.project_direction = project_form['project_direction'].value()
                project.project_short = project_form['project_short'].value()
                project.project_text = project_form['project_text'].value()
                project.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Форма была не полностью заполнена")
        else:
            project_form = ProjectForm(data=dict_project)
            return render(request,'dappx/change_project.html',{'project_form':project_form,})

def review(request):
    projects = ProjectInfo.objects.all()
    return render(request, 'dappx/review.html', {"projects":projects,})

def delete_project(request, name):
    project = ProjectInfo.objects.filter(project_name=name)
    if request.user.username == project[0].project_acount.username:
        project[0].delete()
    return HttpResponseRedirect(reverse('index'))
