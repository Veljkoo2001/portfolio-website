from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    """Lista svih projekata"""
    featured_projects = Project.objects.filter(featured=True)
    other_projects = Project.objects.filter(featured=False)
    
    context = {
        'featured_projects': featured_projects,
        'other_projects': other_projects,
    }
    return render(request, 'projects/list.html', context)

def project_detail(request, slug):
    """Detaljna stranica projekta"""
    project = get_object_or_404(Project, slug=slug)
    
    # Podeli tehnologije u listu
    technologies_list = project.technologies_list()
    
    context = {
        'project': project,
        'technologies_list': technologies_list,
    }
    return render(request, 'projects/detail.html', context)
