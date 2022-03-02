import statistics
from django import urls
from django.conf import settings
from django.urls import path,re_path
from . import views
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name = 'index'),
    path('search/', views.search_image, name='search_image'),
    path('location/<str:search_location>/', views.location_filter, name='location_filter'),
    path('image/<int:image_id>/',views.single,name = 'single'),
     # path('error/',views.error_404,name='error'),   
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

