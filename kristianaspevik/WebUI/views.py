from __future__ import unicode_literals
from .models import Project, Tag, ProjectType
from django.shortcuts import render

def index(request):
    return render(request, 'ui/index.html', {})

def projects_index(request):

    context = {
        'projects': Project.objects.all(),
        'tags': Tag.objects.all(),
        'projecttypes': ProjectType.objects.all()
    }
    return render(request, 'ui/projects/index.html', context)

def about_index(request):
    return render(request, 'ui/index.html', {})

def contact_index(request):
    return render(request, 'ui/contact/index.html', {})

def project_detail(request, project_name):

    project = Project.objects.get(link=project_name)
    return render(request, 'ui/projects/detail.html', {'project': project})
