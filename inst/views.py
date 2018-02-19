# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.forms import UserChangeForm
from .forms import EditProfileForm


def index(request):
    """The home page for Fakestagram"""
    template_name = 'inst/index.html'
    return render(request, template_name)


def photos(request):
    """Show all photos"""
    user_id = request.user
    photos = Photos.objects.filter(owner=user_id)
    context = {'photos': photos}
    return render(request, 'inst/profile_details.html', context)


def settings(request):
    # Show all settings
    user_id = request.user
    setting = UserSettings.objects.filter(user=user_id)
    context = {'settings': setting}
    return render(request, 'inst/settings.html', context)


class SettingsEdit(UpdateView):
    model = UserSettings
    template_name = 'inst/UpdateSettings.html'
    form_class = EditProfileForm

    def get_object(self, queryset=None):
        setting = UserSettings.objects.get(user= self.request.user)
        return setting

    def get_success_url(self):
        return reverse('inst:settings')