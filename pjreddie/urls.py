import os
from django.urls import path
from django.conf import settings
from django.views.generic.base import RedirectView, TemplateView
from django.conf.urls.static import static
import django.views.static

import pjreddie.core.views
import projects.views
import darknet.views
import papers.views
import coqindex.views

from django.contrib import admin
admin.autodiscover()

def redirect(s):
    return RedirectView.as_view(url=s)

def template(s):
    return TemplateView.as_view(template_name=s)

urlpatterns = [
	# Examples:
	# url(r'^$', 'pjreddie.views.home', name='home'),
	# url(r'^pjreddie/', include('pjreddie.foo.urls')),

	path('', pjreddie.core.views.index, name='index'),
	path('projects/pokemon-heart/', redirect('/pokemon-heart/')),
	path('projects/<slug:slug>/', projects.views.project, name='project'),
	path('projects/', projects.views.projects, name='projects'),
	path('coq-tactics/', coqindex.views.index, name='coqindex'),
	path('yolo/', redirect('/darknet/yolo/')),
	path('darknet/', darknet.views.posts, name='posts'),
	path('darknet/<slug:slug>/', darknet.views.post, name='post'),
	path('publications/<slug:slug>/', papers.views.reviews, name='reviews'),
	path('publications/', papers.views.papers, name='papers'),
	path('blog/', pjreddie.core.views.blog, name='blog'),
	path('resume/', redirect('/static/Redmon Resume.pdf')),
    path('pokemon-heart/', template('pokemon.html')),
	# url(r'^reading_list/$', 'readinglist.views.readinglist', name='readinglist'),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	path('admin/', admin.site.urls),
	path('media/<path:path>', django.views.static.serve,
		{'document_root': settings.MEDIA_ROOT}),
	path('static/<path:path>', django.views.static.serve,
		{'document_root': settings.STATIC_ROOT}),
	path('coq-index/<path:path>', django.views.static.serve,
		{'document_root': os.path.join(settings.STATIC_ROOT, 'coq-index')}),
	path('pokemon-heart/<path:path>', django.views.static.serve,
		{'document_root': os.path.join(settings.STATIC_ROOT, 'pokemon')}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
