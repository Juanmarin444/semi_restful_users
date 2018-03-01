from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/new', views.addnew),
    url(r'^user/create', views.create),
    url(r'^user/show/(?P<user_id>\d+)', views.show),
    url(r'^user/destroy/(?P<user_id>\d+)', views.delete),
    url(r'^user/edit/(?P<user_id>\d+)', views.edit),
    url(r'^user/update/(?P<user_id>\d+)', views.update)
]