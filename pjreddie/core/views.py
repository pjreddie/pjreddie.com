# Create your views here.
from django.shortcuts import get_object_or_404, render
from pjreddie.core.models import Project

def index(request):
	return render(request, 'index.html')

def resume(request):
	return render(request, 'resume.html')

def project(request, slug):
	p = get_object_or_404(Project, slug = slug)
	return render(request, 'project.html', {'project':p})

def projects(request):
	p = Project.objects.all().order_by('-start')
	return render(request, 'projects.html', {'projects':p})

def blog(request):
	return render(request, 'blog.html')
