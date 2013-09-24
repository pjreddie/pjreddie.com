# Create your views here.
from django.shortcuts import get_object_or_404, render
from projects.models import Project

def project(request, slug):
	p = get_object_or_404(Project, slug = slug)
	return render(request, 'project.html', {'project':p})

def projects(request):
	p = Project.objects.all().order_by('-start')
	return render(request, 'projects.html', {'projects':p})

