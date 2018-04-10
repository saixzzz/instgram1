from django.conf.urls import url
from . import views
from django.contrib.auth.models import User

"""(?P<username>[\w]+)"""
# (?P<user_id>[\w]+)


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^photos/$', views.Photos.as_view(), name='photos'),

    url(r'^user/profile/$', views.profile, name='profile'),

    url(r'^user/settings/edit$', views.SettingsEdit.as_view(), name='settings_edit'),

    url(r'^user/profile/upload$', views.upload_file, name='upload'),

    url(r'^user/profile/avatar$', views.upload_avatar, name='avatar'),

    url(r'^articles/$', views.article, name='article')


]
