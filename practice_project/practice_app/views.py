from django.shortcuts import render
from practice_app.forms import UserForm,StudentForm
from django.contrib.auth.hashers import make_password,check_password


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def index(request):
    return render(request,'index.html')

def home(request):
    registered=False
    user=UserForm()
    student=StudentForm()
    if request.method=="POST":
        user=UserForm(request.POST)
        student=StudentForm(request.POST)
        if user.is_valid() and student.is_valid():
            user=user.save()
            user.password=make_password(user.password)
            user.save()
            # user.make_password(user.password)
            student.save()
            registered=True
    return render(request,'home.html',{'user':user,'student':student,'registered':registered})

def user_login(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('someone trying login to your Account')
            print('username:{} and password:{}'.format(username,password))
            return HttpResponse("invalid login details")
    else:
        return render(request,'login.html')
