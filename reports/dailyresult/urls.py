from django.conf.urls import url
from dailyresult import views
urlpatterns = [
    url(r'^add_report/$', views.add_report, name='add_report')
]
