import os
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import redirect_to
from django.views.generic.simple import direct_to_template


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'pjreddie.views.home', name='home'),
	# url(r'^pjreddie/', include('pjreddie.foo.urls')),

	url(r'^$', 'pjreddie.core.views.index', name='index'),
	url(r'^projects/pokemon-heart/$', redirect_to, {'url':'/pokemon-heart/'}),
	url(r'^projects/(?P<slug>[-\w]+)/$', 'projects.views.project', name='project'),
	url(r'^projects/$', 'projects.views.projects', name='projects'),
	url(r'^darknet/yolo/$', redirect_to, {'url':'/static/yolo.pdf'}),
	url(r'^darknet/$', 'darknet.views.posts', name='posts'),
	url(r'^darknet/(?P<slug>[-\w]+)/$', 'darknet.views.post', name='post'),
	url(r'^publications/$', 'papers.views.papers', name='papers'),
	# url(r'^reading_list/$', 'readinglist.views.readinglist', name='readinglist'),
	url(r'^blog/$', 'pjreddie.core.views.blog', name='blog'),
	url(r'^resume/$', redirect_to, {'url':'/static/Redmon Resume.pdf'}),
    url(r'^pokemon-heart/$', direct_to_template, { 'template': 'pokemon.html'}),
    url(r'^products/$', direct_to_template, { 'template': 'products.html'}),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	url(r'^admin/', include(admin.site.urls)),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT}),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.STATIC_ROOT}),
	(r'^pokemon-heart/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': os.path.join(settings.STATIC_ROOT, 'pokemon')}),
)
