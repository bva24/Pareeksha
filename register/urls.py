from django.conf.urls import patterns, include, url
from django.contrib import admin
from register import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paresksha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.register),
    url(r'^add-student$', views.add_new_student),
)

