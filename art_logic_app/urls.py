# from django.urls import path
from django.conf.urls import url
from rest_framework import generics

from . import views
from art_logic_app.models import UserAction

urlpatterns = [
    url('api/', views.ArtLogicAPI.as_view() ),
    url(r'^$', views.ArtLogicApp.as_view(), name="art_logic" )
    # url(r'^/api/', generics.ListCreateAPIView.as_view(model=UserAction), name='api')

]
