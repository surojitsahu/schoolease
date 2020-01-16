from django import forms
from accounts.models import School,Tutor,Coaching
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SchoolRegister(forms.ModelForm):
    class Meta:
        model=School
        # fields=['username','password']
        fields = '__all__'



class TutorRegister(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'


class CoachingRegister(forms.ModelForm):
    class Meta:
        model = Coaching
        fields = '__all__'

        # fields=('school_name','school_addesss','smart','general','From_Class')

class SignUpForm(UserCreationForm):
    # category = forms.CharField(max_length=30, required=False, help_text='Optional.')
    name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    phone_number = forms.CharField(max_length=20, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')


    class Meta:
        model = User
        fields = ('name','phone_number', 'email','username', 'password1', 'password2','first_name', )



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

class SchoolRegister(forms.Form):
    school_name = forms.CharField(max_length=50)
    school_addesss = forms.CharField(max_length=50)
    mode= forms.ChoiceField(choices=mode, widget=forms.RadioSelect)
    type= forms.ChoiceField(choices=type, widget=forms.RadioSelect)
    class1 = forms.CharField(label='from class',
                                     widget=forms.Select(choices=class1))
    class12 = forms.CharField(label='to',
                             widget=forms.Select(choices=class2))

    facility = forms.CharField(max_length=50)
    available_stream = forms.CharField(max_length=50)
    board = forms.CharField(label='type of board',
                             widget=forms.Select(choices=board))
    total_student = forms.CharField(label='Total student',max_length=50)
    safety = forms.CharField(label='safety and security measure',max_length=50)
    cctv= forms.ChoiceField(choices=cctv, widget=forms.RadioSelect)

    student_perteacher = forms.CharField(label='Student per Teacher',max_length=50)
    mention = forms.CharField(label='Mention (if anything else)',max_length=50)

    punish = forms.CharField(label='Punishable offence include(optional)',
                             widget=forms.CheckboxSelectMultiple(choices=punish))
    total_teacher = forms.CharField(label='Total Teacher', max_length=50)
    fee = forms.CharField(label='General fee Structure', max_length=50)
    sports = forms.CharField(label='sports played', max_length=50)
    qualification = forms.CharField(label='Qualification Details for Teachers',widget=forms.Textarea)
    facilityes = forms.CharField(label='Facilities Provided',widget=forms.Textarea)
    achievement = forms.CharField(label='Major Achievements',widget=forms.Textarea)
    alumini = forms.CharField(label='here is our Glorious Alumni Network',widget=forms.Textarea)
    idelogy = forms.CharField(label='Our Teaching Ideology is',widget=forms.Textarea)
    future_plans = forms.CharField(label='Our Future Plans & Development are as Follows(optional)',widget=forms.Textarea)
    extra_activity = forms.CharField(label='Do you Support extra Activities',widget=forms.Textarea)
    principle_massage = forms.CharField(label='Principal Message' ,widget=forms.Textarea)
    video = forms.FileField(label='Upload Video')

