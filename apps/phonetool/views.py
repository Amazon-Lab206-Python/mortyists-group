# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "phonetool/index.html")

def register(request):
    result = User.objects.validate_reg(request.POST)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect("/")
    else:
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        return redirect("/phonetool/{}".format(request.session['user_id']))


def login(request):
    result = User.objects.validate_login(request.POST)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        return redirect("/phonetool/{}".format(request.session['user_id']))

def logout(request):
    del request.session['user_id']
    return redirect("/")

def phonetool(request, user_id):
    context ={
        'user': User.objects.get(id=user_id)
    }
    print User.objects.get(id=user_id).location
    return render(request, 'phonetool/phonetool.html', context)

def edit(request, user_id):
    context={
        'user': User.objects.get(id=user_id)
    }
    return render(request, "phonetool/edit.html", context)

def process(request, user_id):
    result = User.objects.validate_edit(request.POST)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect("/")
    else:
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        return redirect("/phonetool/{}".format(request.session['user_id']))
    