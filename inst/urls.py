from django.conf.urls import url
from . import views
from django.contrib.auth.models import User

"""(?P<username>[\w]+)"""
# (?P<user_id>[\w]+)


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^photos/$', views.photos, name='photos'),

    url(r'^(?P<username>[\w]+)$', views.user_profile, name='user_profile'),

    url(r'^user/profile/$', views.profile, name='profile'),

    url(r'^user/settings/edit$', views.SettingsEdit.as_view(), name='settings_edit'),

    url(r'^user/profile/upload$', views.upload_file, name='upload'),

    url(r'^user/profile/avatar$', views.upload_avatar, name='avatar'),

]
