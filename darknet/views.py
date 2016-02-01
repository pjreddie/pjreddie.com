from django.shortcuts import get_object_or_404, render
from darknet.models import Post

def post(request, slug):
	p = get_object_or_404(Post, slug = slug)
	return render(request, 'darknet_post.html', {'post':p})

def posts(request):
	p = Post.objects.filter(visible=True).order_by('order')
	return render(request, 'darknet_main.html', {'posts':p})
