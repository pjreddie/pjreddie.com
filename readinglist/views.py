# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from readinglist.models import Paper, Category
from django.forms import ModelForm

class PaperForm(ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'description', 'link', 'pdf']

def readinglist(request):
    c = Category.objects.all()
    p = Paper.objects.filter(category__isnull=True)
    if request.method == 'POST':
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.category, created = Category.objects.get_or_create(name="Recommended")
            paper.save()
            form = PaperForm()
    else:
        form = PaperForm()
    return render(request, 'readinglist.html', {'categories':c,'uncategorized':p, 'form':form})

