# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import logout, login, authenticate
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import LoginForm, SignUpForm


def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('inst:index'))


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inst:index')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('inst:index')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})
"""
def register(request):
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else:
        # Process complete form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user and then redirect to home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('inst:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
"""
