from .models import UserSettings
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm
from .models import Photos


class EditProfileForm(UserChangeForm):
    class Meta:
        model = UserSettings
        fields = [
            'email',
            'name',
            'web_site',
            'bio',
            'phone_number',
            'password',

        ]
        labels = {'email': 'Email', 'name': 'Full Name', 'web_site': 'Web Site', 'bio': 'Brief info',
                  'phone_number': 'Phone Number', 'password': ''}

    def clean_password(self):
        return ""


class FileForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = [
            'photo',
        ]
