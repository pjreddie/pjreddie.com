from django.conf.urls import patterns, include, url
from django.utils.http import urlquote
from django.utils.encoding import iri_to_uri
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'pjreddie.views.home', name='home'),
	# url(r'^pjreddie/', include('pjreddie.foo.urls')),

	url(r'^$', 'pjreddie.core.views.index', name='index'),
	url(r'^project/(?P<id>\d+)/$', 'pjreddie.core.views.project', name='project'),
	url(r'^projects/$', 'pjreddie.core.views.projects', name='projects'),
	url(r'^blog/$', 'pjreddie.core.views.blog', name='blog'),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	url(r'^admin/', include(admin.site.urls)),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.STATIC_ROOT}),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT}),
)
