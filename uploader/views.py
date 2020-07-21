from django.shortcuts import render, redirect

from .forms import UploadFileForm
from .models import Document
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UploadFileForm()
    return render(request, 'document_form.html', {
        'form': form
    })
