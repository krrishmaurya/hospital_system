from django import forms
from django.shortcuts import redirect, render
from django.views import View
from patient.models import Add_detail,Appointment
from  . import forms
from django.contrib.auth.models import auth

class Home(View):
    def get(self,request):
        content={
            'page_tittle': 'Home',
            'patient_detail':Add_detail.objects.all()
        }
        
        return render(request,'index.html',content)

class Display(View):
    def get(self,request):
        if  request.user.is_authenticated:
            content={
                'page_tittle':'Display',
                'appointments':Appointment.objects.all()

            }
            return render(request,'display_appoint.html',content)
        else:
           content={
               'page_tittle':'Page not found'

           }
           return redirect('/')


class Login(View):
    def get(self,request):
        content={
            'page_tittle':'login page',
            'login':forms.Login()
        }
        return render(request,'login.html',content)

    def post(self,request):
        user_name=request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
        return redirect('/')

class  Logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')        