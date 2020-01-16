"""schoolease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path
from accounts import views
from django.views.generic import TemplateView
from accounts import views
from django.urls import path
from accounts.views import  school_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mytask/',include('mytask.urls')),
    path('',include('django.contrib.auth.urls')),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    # path('signupschool/', TemplateView.as_view(template_name='signupschool.html'), name='signupschool'),
    path('signupcoaching/', views.coachingregisterview, name='signupcoaching'),
    path('signuptutor', views.tutorregisterview, name='signuptutor'),
    path('signupschool', views.schoolregisterview,name='signupschool'),
    path('', school_list_view, name="home"),
    # path('signupschool/', sign_up_view, name="signupschool"),
    path('school_list_view', views.school_list_view, name='school_list_view'),
    # path('login_view', views.login_view, name='login_view'),


    path('aboutus/', TemplateView.as_view(template_name='aboutus.html'), name='aboutus'),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('contactus/', TemplateView.as_view(template_name='contactus.html'), name='contactus'),
    path('accounts/', include('accounts.urls')),  # new
    path('accounts/', include('django.contrib.auth.urls')),

    #path('', views.upload),
    # path('', views.after_login),
]
