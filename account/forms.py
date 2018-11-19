from django import forms
from django.contrib.auth.models import User
from account.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password  = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密码',widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email')

    def clean_password2(self):
        cd =self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('两次密码不相符')
        return cd['password']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date','photo')
