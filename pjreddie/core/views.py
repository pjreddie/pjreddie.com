# Create your views here.
from django.shortcuts import render
from pjreddie.core.models import Project

def index(request):
	
	return render(request, 'index.html')

def project(request, id):
	p = Project.objects.get(id=id)
	return render(request, 'project.html', {'project':p})


def projects(request):
	p = Project.objects.all().order_by('-start')
	return render(request, 'projects.html', {'projects':p})
