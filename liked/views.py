# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from liked.services import add_like, remove_like


def add_user_like(request, obj):
    if request.method == "POST":
        user = request.user
        like = add_like(obj, user)
        context = {"like": like}
        return render(request, 'inst/photos.html', context)
