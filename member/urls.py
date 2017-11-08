from django.conf.urls import url

from . import views

app_name='member'
urlpatterns = [
    url(r'^login$', views.do_login, name='login'),
    url(r'^logout/$', views.do_logout, name='logout'),

    url(r'^member/$', views.MemberListView.as_view(), name='index'),
    url(r'^member/(?P<pk>[0-9]+)/$', views.MemberDetailView.as_view(), name='detail'),

    url(r'^$', views.GroupListView.as_view(), name='group_list'),
    url(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetailView.as_view(), name='group_detail'),

    url(r'^group/(?P<group_id>[0-9]+)/csv/$', views.export_group_to_csv, name='csv_export'),
]
