# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse_lazy
from liked.models import Like
from location.models import Country, City

from smart_selects.db_fields import ChainedForeignKey


class Photos(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, default='Png.png')
    caption = models.TextField(max_length=100, blank=True)
    comment = models.TextField(max_length=200, blank=True)
    likes = GenericRelation(Like)

    class Meta:
        verbose_name_plural = "Photos"

    def __str__(self):
        return "%s`s photo" % self.owner

    def get_absolute_url(self):
        return reverse_lazy("inst:profile", kwargs={'username': self.owner.username})

    @property
    def total_likes(self):
        return self.likes.count()


class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    web_site = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(blank=True, default='Default-image.jpeg')
    email = models.EmailField(blank=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    city = ChainedForeignKey(City, chained_field='country', chained_model_field='country' ,blank=True, null=True)

    class Meta:
        verbose_name_plural = "UserSettings"

    def __str__(self):
        return self.user.username


class Friend(models.Model):
    to_friend = models.ForeignKey(User)
    from_friend = models.ForeignKey(User, related_name='owner', null=True)
    amont = models.PositiveIntegerField()

    class Meta:
        unique_together = ('to_friend', 'from_friend')

    def __str__(self):
        return '{} to {}'.format(self.from_friend, self.to_friend)

    def save(self, *args, **kwargs):
        # self.amont += 1
        super(Friend, self).save(*args, **kwargs)
