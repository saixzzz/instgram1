# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import time, hashlib, random


randomname = hashlib.sha1((str(time.time()) + str(random.randrange(0, 9999999999, 1))).encode('utf-8')).hexdigest()


def get_path_and_name(instance, filename):
    new_name = randomname + ".jpg"
    return new_name


class Photos(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_path_and_name, blank=True)

    def __str__(self):
        return "%s`s photo" % self.owner


class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    web_site = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to=get_path_and_name, blank=True, default='Default-image.jpeg')
    email = models.EmailField(blank=True)

    def __str__(self):
        return "%s`s settings" % self.user


