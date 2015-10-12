from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import Artiste, Album, Morceau
import shlex, subprocess, psutil


# Create your views here.

def index(request):
    artistes = Artiste.objects.all()

    return render_to_response('spotizer/index.html', {'artistes': artistes})


def albums(request, artiste_id):
    artiste = Artiste.objects.get(id=artiste_id)
    mesalbums = Album.objects.all().filter(artiste=artiste_id)

    return render_to_response('spotizer/albums.html', {'artiste': artiste, 'mesalbums': mesalbums})


def morceaux(request, album_id):
    mesmorceaux = Morceau.objects.all().filter(album=album_id)
    album = Album.objects.get(id=album_id)
    artiste = Artiste.objects.get(id=album.artiste.id)

    return render_to_response('spotizer/morceaux.html', {'mesmorceaux': mesmorceaux, 'artiste': artiste})


def status(request):
    args = "/bin/df -h"
    args = shlex.split(args)
    proc = subprocess.Popen(args,stdout=subprocess.PIPE)
    outs = ""
    outs, errs = proc.communicate()

    text = outs.split("\n")

    temp = text[1].split(" ")

    pourcent= temp[0]
    for item in temp:
        if "%" in item:
            pourcent = pourcent +" : " +item




    args = "uptime"
    args = shlex.split(args)
    proc = subprocess.Popen(args,stdout=subprocess.PIPE)
    outs = ""
    outs, errs = proc.communicate()

    cpu = outs

    args = "free -h"
    args = shlex.split(args)
    proc = subprocess.Popen(args,stdout=subprocess.PIPE)
    outs = ""
    outs, errs = proc.communicate()

    text = outs.split("\n")
    temp = text[0].split()
    temp2 = text[1].split()
    temp3 = text[2].split()

    temp[len(temp[2])]

    totalmem = temp2[1]
    occmen = temp3[3]

    totalmem = totalmem[:len(totalmem)-1]
    totalmem = float(totalmem.replace(",", "."))
    occmen = occmen[:len(occmen)-1]
    occmen = float(occmen.replace(",", "."))

    mem = (occmen*100)/(totalmem)
    mem = round(mem,2)
    return render_to_response('spotizer/status.html', {'pourcent': pourcent, 'cpu': cpu, 'mem': mem} )


def stat_psutil(request):

    mem = psutil.virtual_memory()
    mem = mem.percent

    cpu = psutil.cpu_percent(interval=None)

    disk = psutil.disk_usage('/')
    disk = disk.percent




    args = "sensors"
    args = shlex.split(args)
    proc = subprocess.Popen(args,stdout=subprocess.PIPE)
    outs = ""
    outs, errs = proc.communicate()

    text = outs.split("\n")

    temperature = text[2].split(":")[1].split("(")[0]
    temperature = temperature.split("+")[1].split('.')[0]





    return render_to_response('spotizer/stat_psutil.html', {'mem': mem , 'cpu':cpu , 'disk': disk,'temperature' : temperature} )