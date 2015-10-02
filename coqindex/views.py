# Create your views here.
import os
import re
from django.shortcuts import render
from django.conf import settings
from pjreddie.utils import markdown_to_html

def color_words(s, words, color):
    for word in words:
        s = s.replace(word, '<span style="color:%s;">%s</span>'%(color, word))
    return s

def colorify(s):
    red = "#f00"
    purple = "#c0f"
    blue = "#00f"
    green = "#0a0"
    lblue = "#0aa"
    
    s = re.sub(r'Lemma (\w*:)', r'Lemma <span style="color:%s;">\1</span>'%blue, s)
    s = re.sub(r'Inductive (\w*:)', r'Inductive <span style="color:%s;">\1</span>'%blue, s)
    s = re.sub(r'Definition (\w*)', r'Definition <span style="color:%s;">\1</span>'%blue, s)
    s = re.sub(r'Fixpoint (\w*)', r'Fixpoint <span style="color:%s;">\1</span>'%blue, s)
    s = color_words(s, ['Lemma', 'Inductive', 'Definition', 'Fixpoint'], red)
    s = color_words(s, ['forall', 'match', 'with', 'end'], green)
    s = color_words(s, ['Proof.', 'Qed.'], purple)
    s = color_words(s, ['Prop', 'Set'], lblue)
    return s

def index(request):
    filename = os.path.join(settings.STATIC_ROOT, 'coq-index', 'index.md')
    m = open(filename).read()
    html = markdown_to_html(m, [])
    html = colorify(html)
    return render(request, 'coq-index.html', {'html': html})
