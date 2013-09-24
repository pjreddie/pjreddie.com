# Create your views here.
from django.shortcuts import get_object_or_404, render

def index(request):
	return render(request, 'index.html')

def blog(request):
	return render(request, 'blog.html')
