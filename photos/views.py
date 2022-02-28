from django.shortcuts import render,redirect
from .models import Image, Location, Category
from django.http  import HttpResponse, Http404

# Create your views here.
def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'My-art'

    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})