from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    username = forms.CharField(label="Nhập tài khoản")
    password = forms.CharField(widget=forms.PasswordInput, label="Nhập mật khẩu")

    class Meta:
        model = User
        fields = ['username', 'password']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')



