from django.conf.urls import url
from profiles import views
urlpatterns = [
    url(r'^$', views.profiles, name='index'),
    url(r'^(?P<profiles_id>[0-9]+)deatil_info/$', views.profiles_info, name='profiles'),
]
