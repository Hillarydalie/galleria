from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$', views.posted_images, name='postimage'),
    url(r'^$', views.welcome, name='welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    #This is to display a single article on it's own page
    url(r'^image/(\d+)',views.image, name ='image') 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)