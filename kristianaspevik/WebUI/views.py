from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    return render(request, 'UI/index.html', {})

def projects_index(request):

    projects = {
        'test1': '1',
        'test2': '2',
        'test3': '3',
    }
    return render(request, 'UI/projects/index.html', {'projects': projects})

def about_index(request):
    return render(request, 'UI/index.html', {})

def contact_index(request):
    return render(request, 'UI/contact/index.html', {})

def project_detail(request,project_name):
    projects = {
        'test1': '1',
        'test2': '2',
        'test3': '3',
    }

    return render(request, 'UI/projects/index.html', {'projects': projects})