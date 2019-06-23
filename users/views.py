# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm,  UserUpdateForm,ProfileUpdateForm
from .models import Profile
from django.contrib.auth.decorators import login_required





@login_required(login_url='/accounts/login/')

def profile(request):
    if request.method == 'POST':
        u_form =UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Yoour Account has been updated')
            return redirect('profile')
    else:
        u_form =UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        

    context={
        'u_form':u_form,
        'p_form':p_form

     }

    return render(request, 'profiles/profile.html', context)



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            success_url = '/login/'
            messages.success(request, 'Your account has been created! You are now able to log in as an Admin')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})