# Create your views here.
from django.shortcuts import get_object_or_404, render
from papers.models import Paper
from pjreddie.core.models import Page

def index(request):
    p = get_object_or_404(Page, url="index")
    return render(request, 'page.html', {'page':p})

def blog(request):
    return render(request, 'blog.html')

def page(request, url):
	p = get_object_or_404(Page, url = url)
	return render(request, 'page.html', {'page':p})
