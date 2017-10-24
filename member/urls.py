from django.conf.urls import url

from . import views

app_name='member'
urlpatterns = [
    url(r'^$', views.ListView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
