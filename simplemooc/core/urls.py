from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^', include('simplemooc.core.urls)),
   url(r'^contato/$', 'simplemooc.core.views.contact', name='contact'),
)
