# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.views.generic import UpdateView, FormView
from django.core.urlresolvers import reverse
from .models import *
from .assist import ImageCropper
from .forms import EditProfileForm, FileForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from instgram1.settings import BASE_DIR
from django.http import HttpResponseRedirect

randomname = hashlib.sha1((str(time.time()) + str(random.randrange(0, 9999999999, 1))).encode('utf-8')).hexdigest()

base_forder = BASE_DIR + '/media/photos/'
base_folder_x05 = BASE_DIR + '/media/photos/crop_x0.5/'
base_folder_x1 = BASE_DIR + '/media/photos/crop_x1/'
base_folder_x2 = BASE_DIR + '/media/photos/crop_x2/'


def index(request):
    """The home page for Fakestagram"""
    template_name = 'inst/index.html'
    return render(request, template_name)


"""
def gallery(request):
    path = base_folder_x1
    img_list = os.listdir(path)
    context = {'images': img_list}

    return render_to_response('inst/photos.html', context)
"""


@login_required
def photos(request):
    """Show all photos"""
    photos = Photos.objects.filter(owner=request.user)
    context = {'images': photos}
    return render(request, 'inst/photos.html', context)


@login_required
def profile(request):
    """Show all settings"""
    user_id = request.user
    # photos = Photos.objects.filter(owner=user_id).filter(photo__exact='.jpeg')
    setting = UserSettings.objects.filter(user=user_id)
    context = {'setting': setting}
    return render(request, 'inst/profile.html', context)

"""
def upload_file(request):
    if request.method == 'POST' and request.FILES['photo']:
        form = FileForm(request.FILES)
        file = request.FILES['photo']
        cropper = ImageCropper()
        cropped = cropper.crop_x1(file)
        if form.is_valid():
            instance = Photos(photo=file, owner=request.user)
            instance.save()
            return HttpResponseRedirect('/user/profile/')

    else:
        form = FileForm()
    return render(request, 'inst/upload.html', {'form': form})
"""


@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES['photo']:
        myfile = request.FILES['photo']
        fs = FileSystemStorage()
        filename1 = fs.save(base_folder_x1 + myfile.name, myfile)
        filename2 = fs.save(base_folder_x2 + myfile.name, myfile)
        cropper = ImageCropper()
        cropper.crop_x1(filename1)
        cropper.crop_x2(filename2)
        instance = Photos(photo=myfile.name, owner=request.user)
        instance.save()
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
        filename = fs.save(base_folder_x05 + randomname + '.jpg', myfile)
        photo = UserSettings.objects.filter(user=request.user).update(avatar=filename)
        uploaded_file_url = fs.url(filename)
        cropper = ImageCropper()
        cropper.crop_x05(base_folder_x05 + randomname + '.jpeg')
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
