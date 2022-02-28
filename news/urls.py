import statistics
from django import urls
from django.conf import settings
from django.urls import path,re_path
from . import views



urlpatterns=[
    path('',views.index,name = 'index'),
    path(r'^search/', views.search_image, name='search_image'),
    path(r'^location/(?P<image_location>\d+)', views.location_filter, name='location_filter'),
    path(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single,name = 'single')
]