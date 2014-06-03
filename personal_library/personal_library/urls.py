#-*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personal_library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'library.views.index', name='index'),
    url(r'^save/$', 'library.views.save', name='book.save'),
    url(r'^edit/(?P<book_id>\d+)[/]$', 'library.views.edit', name='book.edit'),
    url(r'^remove/(?P<book_id>\d+)[/]$', 'library.views.remove', name='book.remove'),
    
    url(r'^admin/', include(admin.site.urls)),
)
