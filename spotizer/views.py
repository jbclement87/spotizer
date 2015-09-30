from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import Artiste, Album, Morceau

# Create your views here.

def index(request):
    artistes = Artiste.objects.all()

    return render_to_response('spotizer/index.html', {'artistes': artistes})


def albums(request, artiste_id):
    artiste = Artiste.objects.get(id=artiste_id)
    mesalbums = Album.objects.all().filter(artiste=artiste_id)

    return render_to_response('spotizer/albums.html', {'artiste':artiste,'mesalbums': mesalbums})


def morceaux(request, album_id):
    mesmorceaux = Morceau.objects.all().filter(album=album_id)

    return render_to_response('spotizer/morceaux.html', {'mesmorceaux':mesmorceaux})