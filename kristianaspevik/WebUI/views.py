from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.template import loader

def index(request):
    return render(request, 'UI/index.html', {})

def projects_index(request):
    return None

def about_index(request):
    return None
