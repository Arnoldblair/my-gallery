import statistics
from django import urls
from django.conf import settings
from django.urls import path,re_path
from . import views



urlpatterns=[
    path('',views.index,name = 'index'),
    path('', views.search_image, name='search_image'),
    path('', views.location_filter, name='location_filter'),
    path('',views.single,name = 'single')
]