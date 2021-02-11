from django import forms

from practice_app.models import Userinfo
from practice_app.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('name','portfolio')


class UserForm(forms.ModelForm):
    class Meta:
        model=Userinfo
        fields=('username','email','password')
