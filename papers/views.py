# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from papers.models import Paper
from django.forms import ModelForm

def papers(request):
    p = Paper.objects.all().order_by('-date')
    return render(request, 'papers.html', {'papers':p})

def reviews(request, slug):
    p = get_object_or_404(Paper, slug = slug)
    return render(request, 'reviews.html', {'paper':p})

