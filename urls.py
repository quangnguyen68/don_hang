from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='dashboard'),
    path('kh=<id>/dh=<id2>', views.khach_hang,name='kh'),
