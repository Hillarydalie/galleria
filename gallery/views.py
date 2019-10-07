from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image
import datetime as dt

# Create your views here.
def welcome(request):
    photos = Image.get_photos()
    return render(request, 'index.html', {"photos":photos})

def posted_images(request):
    date = dt.date.today()
    photos = Image.todays_images()
    return render(request, 'index.html', {"date":date, "photos":photos})

# Search function.
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})
    