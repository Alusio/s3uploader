from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

from s3uploader import settings
from .forms import UploadFileForm
from .models import Document


@login_required
@transaction.atomic
def index(request):
    documents = Document.objects.order_by('-uploaded_at').all()[:30]
    return render(request, 'index.html', {'documents': documents, 'title': settings.NAME})


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('upload')
        if form.is_valid():
            for file in files:
                doc = Document(upload=file, user=request.user, device=getOS(request))
                doc.save()
            return redirect('index')
    else:
        form = UploadFileForm()
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
