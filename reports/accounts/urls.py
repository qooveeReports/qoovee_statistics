from django.conf.urls import url
from accounts import views
urlpatterns = [
    url(r'^registrations/$', views.register, name='register'),
    url(r'^login/$', views.authentication, name='login')
]
