from django import forms
from django.forms import HiddenInput

from uploader.models import Document


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('upload',)

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['upload'].widget.attrs \
            .update({
            'class': 'upload-input'
        })
