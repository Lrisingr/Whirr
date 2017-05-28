from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Album,Songs
from django.template import loader
#serialize to Iterate over model column names and values in template
from django.core import serializers


# Create your views here.
def index(request):
    #to iterate over all columns in the model
    Avail_albums =  Album.objects.all()
    meta_names = Album._meta.fields
    #to iterate over selected column names
    #Avail_albums = serializers.serialize( "python", Album.objects.all(),fields = ('album_title','album_artist))
    context = {
        'avail_albums' : Avail_albums,
        'columns_name' : meta_names
    }
    return render(request,'music/index.html',context)

#details of particular album when selected
def details(request,album_id):
    try:
        returned_album = Album.objects.get(pk=album_id)
        song_columns = Songs._meta.fields
        #serializers.serialize( "python", Songs.objects.all(),fields = ('song_title','song_artist','song_length'))
    context = {
        'album': returned_album,
        'song_columns':song_columns
    }
    except Album.DoesNotExist:
        raise Http404("Albumm No longer exists")
    return render(request,'music\Details.html',context)