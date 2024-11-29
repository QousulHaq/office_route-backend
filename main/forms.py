from django import forms
from django.contrib.auth.models import User
from main.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta():
        model = User
        fields = ('username', 'email', 'password',)
        # fields = ('username', 'email', 'password', 'first_name', 'last_name')
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
        # fields = ('profile_pic', 'first_name', 'last_name')