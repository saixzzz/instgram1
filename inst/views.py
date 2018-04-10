# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView
from django.core.urlresolvers import reverse
from .models import *
from .assist import ImageCropper
from .forms import EditProfileForm, FileForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from instgram1.settings import BASE_DIR
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

randomname = hashlib.sha1((str(time.time()) + str(random.randrange(0, 9999999999, 1))).encode('utf-8')).hexdigest()

base_folder = BASE_DIR + '/media/photos/'
avatar = BASE_DIR + '/media/photos/avatar/'
base_folder_x1 = BASE_DIR + '/media/photos/crop_x1/'
base_folder_x2 = BASE_DIR + '/media/photos/crop_x2/'


def index(request):
    """The home page for Fakestagram"""
    template_name = 'inst/index.html'
    return render(request, template_name)


class Photos(ListView):
    model = Photos
    paginate_by = 6
    context_object_name = 'photos'
    template_name = 'inst/photos.html'


@login_required
def profile(request):
    """Show all settings"""
    user_id = request.user
    photos = Photos.objects.filter(owner=request.user)
    setting = UserSettings.objects.filter(user=user_id)
    context = {'setting': setting, 'images': photos}
    return render(request, 'inst/profile.html', context)


def upload_file(request):
    if request.method == 'POST' and request.FILES['photo']:
        myfile = request.FILES['photo']
        fs = FileSystemStorage()
        filename1 = fs.save(base_folder_x1 + myfile.name, myfile)
        filename2 = fs.save(base_folder_x2 + myfile.name, myfile)
        cropper = ImageCropper()
        cropper.crop_x1(filename1)
        cropper.crop_x2(filename2)
        Photos(owner=request.user, photo=myfile.name)
        uploaded_file_url = fs.url(myfile)
        return render(request, 'inst/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
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
        return render(request, 'inst/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
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


def article(request):
    numbers_list = range(1, 1000)
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'inst/articles.html', {'numbers': numbers})
