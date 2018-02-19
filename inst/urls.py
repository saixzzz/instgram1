from django.conf.urls import url
from . import views
from django.contrib.auth.models import User

"""(?P<username>[\w]+)"""
# (?P<user_id>[\w]+)


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^photos/$', views.photos, name='profile_details'),

    url(r'^user/settings/$', views.settings, name='settings'),

    url(r'^user/settings/edit$', views.SettingsEdit.as_view(), name='settings_edit'),
]
