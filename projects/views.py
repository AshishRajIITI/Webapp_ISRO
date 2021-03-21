from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def documentation(request, pk):
    project = Project.objects.get()
    context = {
        'project': project
    }
    return render(request, 'documentation.html', context)