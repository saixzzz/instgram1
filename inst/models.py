# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

from liked.models import Like


def get_name_and_path():
    pass


class Photos(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='', blank=True, default='Png.png')
    caption = models.TextField(max_length=100, blank=True)
    comment = models.TextField(max_length=200, blank=True)
    likes = GenericRelation(Like)

    def __str__(self):
        return "%s`s photo" % self.owner

    @property
    def likes_count(self):
        return self.likes.count()


class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    web_site = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(blank=True, default='Default-image.jpeg')
    email = models.EmailField(blank=True)

    def __str__(self):
        return "%s`s settings" % self.user


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    @classmethod
    def delete_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)
