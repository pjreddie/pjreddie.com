# Create your views here.
from django.shortcuts import render
from pjreddie.core.models import Post

def index(request):
	
	return render(request, 'index.html')

def post(request, id):
	p = Post.objects.get(id=id)
	return render(request, 'post.html', {'post':p})
