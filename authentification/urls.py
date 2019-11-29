from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = "authentification"

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    # url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

]
