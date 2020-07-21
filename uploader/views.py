from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

from .forms import UploadFileForm
from .models import Document
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage


@login_required
@transaction.atomic
def index(request):
    documents = Document.objects.all()
    return render(request, 'index.html', {'documents': documents})


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UploadFileForm()
    return render(request, 'document_form.html', {
        'form': form
    })
