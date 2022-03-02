from django.urls import path,include,re_path
from django.contrib import admin
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls'))

]