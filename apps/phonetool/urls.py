from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^phonetool/(?P<user_id>\d+)$', views.phonetool),
    url(r'^phonetool/(?P<user_id>\d+)/edit$', views.edit),    
    url(r'^phonetool/(?P<user_id>\d+)/edit/process$', views.process),
    url(r'^phonetool/(?P<user_id>\d+)/roll$', views.roll),            
]