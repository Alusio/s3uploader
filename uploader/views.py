from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

from s3uploader import settings
from .forms import DocumentForm, AudioForm, VideoForm, ZipForm, PictureForm
from .models import Document, Audio, Video, Zip, Picture


@login_required
@transaction.atomic
def index(request):
    documents = Document.objects.order_by('-uploaded_at').all()[:30]
    audios = Audio.objects.order_by('-uploaded_at').all()[:30]
    videos = Video.objects.order_by('-uploaded_at').all()[:30]
    zips = Zip.objects.order_by('-uploaded_at').all()[:30]
    pictures = Picture.objects.order_by('-uploaded_at').all()[:30]
    return render(request, 'index.html',
                  {'documents': documents, 'audios': audios, 'videos': videos, 'zips': zips, 'pictures': pictures,
                   'title': settings.NAME})


@login_required
def upload(request, type):
    if request.method == 'POST':
        if type == "audio":
            form = AudioForm(request.POST, request.FILES)
        elif type == "video":
            form = VideoForm(request.POST, request.FILES)
        elif type == "zip":
            form = ZipForm(request.POST, request.FILES)
        elif type == "picture":
            form = PictureForm(request.POST, request.FILES)
        else:
            form = DocumentForm(request.POST, request.FILES)
        files = request.FILES.getlist('upload')
        if form.is_valid():
            for file in files:
                print(file)
                if type == "audio":
                    doc = Audio(upload=file, user=request.user, device=getOS(request), name=file)
                elif type == "video":
                    doc = Video(upload=file, user=request.user, device=getOS(request), name=file)
                elif type == "zip":
                    doc = Zip(upload=file, user=request.user, device=getOS(request), name=file)
                elif type == "picture":
                    doc = Picture(upload=file, user=request.user, device=getOS(request), name=file)
                else:
                    doc = Document(upload=file, user=request.user, device=getOS(request), name=file)

                doc.save()
            return redirect('index')
    else:
        if type == "audio":
            form = AudioForm()
        elif type == "video":
            form = VideoForm()
        elif type == "zip":
            form = ZipForm()
        elif type == "picture":
            form = PictureForm()
        else:
            form = DocumentForm()

    return render(request, 'document_form.html', {
        'form': form,
        'title': settings.NAME})


def getOS(request):
    if request.Windows:
        return "Windows"
    elif request.Linux:
        return "Linux"
    elif request.iMac:
        return "iMac"
    elif request.iPhone:
        return "iPhone"
    elif request.iPad:
        return "iPad"
    elif request.iPod:
        return "iPod"
    elif request.Android:
        return "Android"
    else:
        return "NaN"
