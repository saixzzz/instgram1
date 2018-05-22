from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.views.generic import UpdateView, ListView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db.models import Count, Prefetch

from .models import UserSettings, Photos, Friend
from .forms import EditProfileForm, EntryForm
from instgram1.settings import BASE_DIR

from .services import ImageCropper
from location.models import City, Country

base_folder = BASE_DIR + '/media/photos/'
avatar = BASE_DIR + '/media/photos/avatar/'
base_folder_x1 = BASE_DIR + '/media/photos/crop_x1/'
base_folder_x2 = BASE_DIR + '/media/photos/crop_x2/'
base_folder_x3 = BASE_DIR + '/media/photos/crop_x3/'


def index(request):
    """The home page for Fakestagram"""
    template_name = 'inst/index.html'
    return render(request, template_name)


def friendsleaderb(request):
    query = Prefetch('friend_set', Friend.objects.distinct())
    count = User.objects.prefetch_related(query).annotate(number_of_friends=Count('friend'))
    users = User.objects.all().order_by()
    # friends = Friend.objects.all()
    context = {'users': users}
    return render(request, 'inst/top.html', context)


@login_required
def photos(request):
    """Show all feed"""
    photos = Photos.objects.filter(owner=request.user)
    setting = UserSettings.objects.filter(user=request.user)
    context = {'setting': setting, 'images': photos}
    return render(request, 'inst/photos.html', context)


def user_profile(request, username):
    username = username.title()
    photos = Photos.objects.filter(owner__username=username)
    setting = UserSettings.objects.filter(user__username=username)
    user_id = User.objects.get(username=username).id
    context = {'user_setting': setting, 'images': photos, 'user_name': username, 'user_id': user_id, 'friendships': ''}
    return render(request, 'inst/user_profile.html', context)


def add_or_remove_friend(request, pk):
    new_friend = User.objects.get(id=pk)
    friendship = Friend(to_friend=new_friend, from_friend=request.user, amont=+1)
    friendship.save()
    return redirect('inst:index')


"""
def search(request):
    if request.method == "GET":
        query = request.GET.get("q", None)
        if query is not None:
            searched = User.objects.filter(username__icontains=query)
            context = {'user': searched}
        return render(request, 'inst/search_results.html', context)
"""


@login_required
def profile(request):
    """Show all settings"""
    photos = Photos.objects.filter(owner=request.user)
    setting = UserSettings.objects.filter(user=request.user)
    context = {'setting': setting, 'images': photos, 'user_name': request.user}
    return render(request, 'inst/profile.html', context)


@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('photo'):
        caption = request.POST.get('caption')
        myfile = request.FILES.get('photo')

        # saves uploaded file
        fs = FileSystemStorage()
        filename1 = fs.save(base_folder_x1 + myfile.name, myfile)
        filename2 = fs.save(base_folder_x2 + myfile.name, myfile)
        filename3 = fs.save(base_folder_x3 + myfile.name, myfile)

        # crops uploaded image to 3 presets
        cropper = ImageCropper()
        cropper.crop_x1(filename1)
        cropper.crop_x2(filename2)
        cropper.crop_x3(filename3)

        # saving filename to database
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
        user = self.request.user
        setting = UserSettings.objects.get(user=user)
        return setting

    def get_success_url(self):
        return reverse('inst:profile')


def load_cities(request):
    country = request.GET.get('country')
    cities = City.objects.filter(country__exact=country).order_by('name')
    context = {'cities': cities}
    return render(request, 'inst/city_dropdown_list_options.html', context)
