from django.conf.urls import patterns, include, url
from django.conf import settings


#admin.site.unregister(Site)



#if settings.DEBUG:
urlpatterns = patterns('',
	('^(?P<flag>.+)/(?P<app>.+)/(?P<model>.+)/(?P<mid>.+)/(?P<field>.+)/', 'translatable_content.views.data'),

)

