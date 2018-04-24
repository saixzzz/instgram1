from django.conf.urls import url
from . import views
from django.contrib.auth.models import User

"""(?P<username>[\w]+)"""
# (?P<user_id>[\w]+)


urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Displays feed
    url(r'^photos/$', views.photos, name='photos'),

    # url(r'^api/photos/like$', views.PostLikeToggle.as_view(), name='like-api-toggle'),

    # Displays users profile
    url(r'^(?P<username>[\w]+)$', views.user_profile, name='user_profile'),

    # Displays your own profile
    url(r'^user/profile/$', views.profile, name='profile'),

    # Allows to edit your settings
    url(r'^user/settings/edit$', views.SettingsEdit.as_view(), name='settings_edit'),

    # photo upload
    url(r'^user/profile/upload$', views.upload_file, name='upload'),

    # avatar upload function
    url(r'^user/profile/avatar$', views.upload_avatar, name='avatar'),

    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)', views.change_friends, name='change_friends')

]
