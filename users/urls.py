"""Defines URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    # Login page
    url(r'^login/$', views.login_view, name='login'),

    # Logout page
    url(r'^logout/$', views.logout_view, name='logout'),

    # Registration page
    url(r'^register/$', views.register, name='register'),

    url(r'^password/$', views.change_password, name='change_password')

]