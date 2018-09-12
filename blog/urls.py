from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url(r'^message/$', views.message_view, name='message'),
]
