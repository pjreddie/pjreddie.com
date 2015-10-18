# Create your views here.
import os
import re
from django.shortcuts import render
from django.conf import settings
from pjreddie.utils import markdown_to_html

ROOT = os.path.dirname(os.path.realpath(__file__))

def get_path(p):
	return os.path.join(ROOT, p)


def color_words(s, words, color):
    for word in words:
        s = s.replace(word, '<span class="%s">%s</span>'%(color, word))
    return s

def colorify(s):
    red = "coq_red"
    purple = "coq_purple"
    blue = "coq_blue"
    green = "coq_gren"
    lblue = "coq_lblue"
    
    s = re.sub(r'Lemma (\w*:)', r'Lemma <span class="%s">\1</span>'%blue, s)
    s = re.sub(r'Inductive (\w*:)', r'Inductive <span class="%s">\1</span>'%blue, s)
    s = re.sub(r'Definition (\w*)', r'Definition <span class="%s">\1</span>'%blue, s)
    s = re.sub(r'Fixpoint (\w*)', r'Fixpoint <span class="%s">\1</span>'%blue, s)
    s = color_words(s, ['Lemma', 'Inductive', 'Definition', 'Fixpoint'], red)
    s = color_words(s, ['forall', 'match', 'with', 'end'], green)
    s = color_words(s, ['Proof.', 'Qed.'], purple)
    s = color_words(s, ['Prop', 'Set'], lblue)
    return s

def index(request):
    filename = get_path('index.md')
    m = open(filename).read()
    html = markdown_to_html(m, [])
    html = colorify(html)
    return render(request, 'coqindex.html', {'html': html})
