from django import forms
from django.forms import HiddenInput

from uploader.models import Document


class UploadFileForm(forms.ModelForm):
    upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Document
        fields = ('upload',)