# Create your views here.
from django.shortcuts import get_object_or_404, render
from papers.models import Paper

def index(request):
    p = Paper.objects.all().order_by('-date')
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')
