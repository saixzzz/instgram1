# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import operator
from functools import reduce
from django.shortcuts import render, render_to_response
from django.views.generic import UpdateView, FormView
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import UpdateView, ListView
from django.core.urlresolvers import reverse
from .models import *
from .assist import ImageCropper
from .forms import EditProfileForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from instgram1.settings import BASE_DIR
from django.db.models import Q
from django.http import HttpResponseRedirect

base_folder = BASE_DIR + '/media/photos/'
avatar = BASE_DIR + '/media/photos/avatar/'
base_folder_x1 = BASE_DIR + '/media/photos/crop_x1/'
base_folder_x2 = BASE_DIR + '/media/photos/crop_x2/'
base_folder_x3 = BASE_DIR + '/media/photos/crop_x3/'


def index(request):
    """The home page for Fakestagram"""
    template_name = 'inst/index.html'
    return render(request, template_name)


@login_required
def photos(request):
    """Show all feed"""
    photos = Photos.objects.filter(owner=request.user)
    setting = UserSettings.objects.filter(user=request.user)
    context = {'setting': setting, 'images': photos}
    return render(request, 'inst/photos.html', context)


def user_profile(request, username):
    photos = Photos.objects.filter(owner__username=username)
    setting = UserSettings.objects.filter(user__username=username)
    context = {'setting': setting, 'images': photos}
    return render(request, 'inst/profile.html', context)


def change_friends(request, operation, pk):
    new_friend = Friend.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'rem':
        Friend.delete_friend(request.user, new_friend)


@login_required
def profile(request):
    """Show all settings"""
    photos = Photos.objects.filter(owner=request.user)
    setting = UserSettings.objects.filter(user=request.user)
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    except Friend.DoesNotExist:
        friends = None
    context = {'setting': setting, 'images': photos, 'friends': friends}
    return render(request, 'inst/profile.html', context)


@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES['photo']:
        caption = request.POST['caption']
        myfile = request.FILES['photo']
        fs = FileSystemStorage()
        filename1 = fs.save(base_folder_x1 + myfile.name, myfile)
        filename2 = fs.save(base_folder_x2 + myfile.name, myfile)
        filename3 = fs.save(base_folder_x3 + myfile.name, myfile)
        cropper = ImageCropper()
        cropper.crop_x1(filename1)
        cropper.crop_x2(filename2)
        cropper.crop_x3(filename3)
        instance = Photos(photo=myfile.name, owner=request.user, caption=caption)
        instance.save()
        uploaded_file_url = fs.url(myfile)
        return render(request, 'inst/upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'inst/upload.html')


@login_required
def upload_avatar(request):
    if request.method == 'POST' and request.FILES['photo']:

        myfile = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(avatar + myfile.name, myfile)
        cropper = ImageCropper()
        cropper.crop_x1(filename)
        UserSettings.objects.filter(user=request.user).update(avatar=myfile.name)
        uploaded_file_url = fs.url(filename)
        return render(request, 'inst/upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'inst/upload.html')


class SettingsEdit(UpdateView):
    model = UserSettings
    template_name = 'inst/UpdateSettings.html'
    form_class = EditProfileForm

    def get_object(self, queryset=None):
        setting = UserSettings.objects.get(user=self.request.user)
        return setting

    def get_success_url(self):
        return reverse('inst:profile')
