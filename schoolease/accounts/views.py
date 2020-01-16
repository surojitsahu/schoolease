from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from accounts.models import School,Tutor,Coaching
from accounts import forms
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect
from.forms import SignUpForm
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect





def schoolregisterview(request):
    form = forms.SchoolRegister()
    if request.method=='POST':
        form = forms.SchoolRegister(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'signupschool.html',{'form':form})



def school_list_view(request):
    school_list=School.objects.all()
    tutor_list = Tutor.objects.all()
    coaching_list = Coaching.objects.all()
    return render(request,'home.html',{'school_list':school_list,'tutor_list':tutor_list,'coaching_list':coaching_list})


def tutorregisterview(request):
    form = forms.TutorRegister()
    if request.method=='POST':
        form = forms.TutorRegister(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'signuptutor.html',{'form':form})


def coachingregisterview(request):
    form = forms.CoachingRegister()
    if request.method=='POST':
        form = forms.CoachingRegister(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'signupcoaching.html',{'form':form})



class signupcoaching(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signupcoaching.html'


class signuptutor(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signuptutor.html'


def thankyou(request):
    return render(request,'home.html')


