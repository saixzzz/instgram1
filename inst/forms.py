from .models import UserSettings
from django import forms
from .models import Photos
from location.models import City


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = [
            'email',
            'name',
            'web_site',
            'bio',
            'phone_number',
            'country',
            'city',

        ]
        labels = {'email': 'Email', 'name': 'Full Name', 'web_site': 'Web Site', 'bio': 'Brief info',
                  'phone_number': 'Phone Number', }


class EntryForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['comment']
        labels = {'comment': ''}
