from django.db import models
from django import forms

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
# Create your models here.
#


mode=[('select1','smart'),
         ('select2','general')]

type=[('select1','Coed'),
         ('select2','boys'),('select3','girls')]

class1= [
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('7th', '7th'),
    ]

class2= [
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('12th', '12th'),
    ]

board= [
    ('1st', 'state'),
    ('2nd', 'CBSE'),
    ('3rd', 'ICSE'),
    ('4th', 'Others'),

    ]
cctv= [
    ('1st', 'present'),
    ('2nd', 'not present'),
    ]

punish= [
    ('1st', 'misbehave'),
    ('2nd', 'damage to property'),
    ('3rd', 'fighting'),
    ('4th', 'late arrivels'),]



class School(models.Model):
    school_name=models.CharField(max_length=50,blank=True)
    # password = models.CharField(max_length=50,blank=True)
    school_addesss=models.CharField(max_length=50,blank=True)
    smart= models.BooleanField('smart',blank=True)
    general= models.BooleanField('general',blank=True)
    From_Class=models.CharField(max_length=10,choices=class1,blank=True)
    to=models.CharField(max_length=10,choices=class2,blank=True)
    Commuting_Facilities = models.CharField(max_length=50,blank=True)
    Available_stream_after_10th = models.CharField(max_length=50,blank=True)
    Type_of_Board=models.CharField(max_length=10,choices=board,blank=True)
    Total_Students = models.CharField(max_length=50,blank=True)
    Safety_Security_and_Meausures = models.CharField(max_length=50,blank=True)
    CCTV= models.BooleanField('Present',blank=True)
    CCTV1= models.BooleanField('Not Present',blank=True)
    Students_per_Teachers = models.CharField(max_length=50,blank=True)
    Mention = models.CharField(max_length=50,blank=True)
    Misbehaving= models.BooleanField('Misbehaving',blank=True)
    Damege_to_Property= models.BooleanField('Damege_to_Property',blank=True)
    Fighting= models.BooleanField('Fighting',default=False)
    Late_Arrivels= models.BooleanField('Late_Arrivels',default=False)
    Fee_Structure = models.CharField(max_length=50,blank=True)
    Sports_Played = models.CharField(max_length=50,blank=True)
    Qualification_Details_of_Teachers= models.TextField(max_length=50,blank=True)
    Facilities_Provided= models.TextField(max_length=50,blank=True)
    Major_Achivements= models.TextField(max_length=50,blank=True)
    Glorious_Alumini_Network= models.TextField(max_length=50,blank=True)
    Our_Teachings_Ideology= models.TextField(max_length=50,blank=True)
    Our_future_Plans_Development= models.TextField(max_length=50,blank=True)
    Do_you_support_any_Extra_Activities= models.TextField(max_length=50,blank=True)
    Principle_Message= models.TextField(max_length=50,blank=True)
    upload_video=models.FileField(blank=True)


class Tutor(models.Model):
    Name=models.CharField(max_length=50,blank=True)
    addesss=models.CharField(max_length=50,blank=True)
    Phone_number = models.IntegerField(blank=True)
    Email_id = models.EmailField(blank=True)
    Timings=models.CharField(max_length=10,blank=True)
    Subjects = models.CharField(max_length=50,blank=True)
    Class_being_Tought = models.CharField(max_length=50,blank=True)
    Years_of_Experience = models.CharField(max_length=50,blank=True)
    Educationnal_Qualification = models.CharField(max_length=50,blank=True)
    Fees = models.IntegerField(blank=True)
    Frequency_of_Class = models.CharField(max_length=50,blank=True)
    About= models.TextField(max_length=50,blank=True)


class Coaching(models.Model):
    Name=models.CharField(max_length=50,blank=True)
    addesss=models.CharField(max_length=50,blank=True)
    Phone_number = models.IntegerField(blank=True)
    Email_id = models.EmailField(blank=True)
    Timings=models.CharField(max_length=10,blank=True)
    Subjects = models.CharField(max_length=50,blank=True)
    Class_being_Tought = models.CharField(max_length=50,blank=True)
    Years_of_Experience = models.CharField(max_length=50,blank=True)
    Educationnal_Qualification = models.CharField(max_length=50,blank=True)
    Fees = models.IntegerField(blank=True)
    Frequency_of_Class = models.CharField(max_length=50,blank=True)
    About= models.TextField(max_length=50,blank=True)


