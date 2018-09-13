from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    # url(r'^message/$', views.message_view, name='message'), //메시지 텔레그램으로 보내는거는 자바스크립트로 처리
]
