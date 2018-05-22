from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Enter Login'}), label='')

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter Password'}), label='')


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Enter Login'}), label='')

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Enter Email'}), label='')

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Enter Password'}), label='')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Confirm Password'}), label='')


class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Enter Old Password'}), label='')

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Enter New Password'}), label='')

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Confirm New Password'}), label='')


