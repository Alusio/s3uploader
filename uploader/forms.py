from django import forms
from django.forms import HiddenInput

from uploader.models import Document, Video, Audio, Zip, Picture


class DocumentForm(forms.ModelForm):
    upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Document
        fields = ('upload',)


class VideoForm(forms.ModelForm):
    upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Video
        fields = ('upload',)


class AudioForm(forms.ModelForm):
    upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Audio
        fields = ('upload',)


class ZipForm(forms.ModelForm):
    upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Zip
        fields = ('upload',)


class PictureForm(forms.ModelForm):
    upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Picture
        fields = ('upload',)
