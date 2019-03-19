from django.conf.urls import url
from . import views

app_name = 'example'

urlpatterns = [
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^signup/$', views.sign_up, name='signup'),
    url(r'^$', views.user_list, name='user_list'),
]
