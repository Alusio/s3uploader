from django import forms

from uploader.models import Document


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('upload', )