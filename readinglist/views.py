# Create your views here.
from django.shortcuts import get_object_or_404, render
from readinglist.models import Paper

def readinglist(request):
	p = Paper.objects.all().order_by('-date_added')
	return render(request, 'readinglist.html', {'papers':p})

