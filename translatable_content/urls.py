from django.conf.urls import patterns, include, url
from django.conf import settings


#admin.site.unregister(Site)



#if settings.DEBUG:
urlpatterns = patterns('',
	('^data/(?P<app>.+)/(?P<model>.+)/(?P<mid>.+)/(?P<field>.+)/$', 'content_translation.views.data'),
	(r'^static/(?P<path>.*)$','django.views.static.serve',{}),
)

#urlpatterns += patterns('',
#    # ... the rest of your URLconf goes here ...
#	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  settings.STATIC_ROOT}),
# 
# )

