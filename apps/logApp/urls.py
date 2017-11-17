from django.conf.urls import url
from . import views

urlpatterns= [
	url(r'^$', views.index),
	url(r'^register$', views.new),
	url(r'^success$', views.success),
	url(r'^signin$', views.signin),
	url(r'^logout$', views.logout),
]