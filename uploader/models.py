from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
import os


def document_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')


def video_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4', '.avi', '.3gp', '.ogg', '.wmv', '.flv']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')


def audio_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp3', '.wav', '.flac']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')


def zip_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.zip', ]
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')


def picture_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg', '.gif', '.png', '.webp', '.jpg']
    if not ext in valid_extensions:
        raise ValidationError(u'File not supported!')


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=100, blank=True, null=True)
    upload = models.FileField(upload_to='documents', validators=[document_validator])
    device = models.TextField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.upload.name


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=100, blank=True, null=True)
    upload = models.FileField(upload_to='videos', validators=[video_validator])
    device = models.TextField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.upload.name


class Audio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=100, blank=True, null=True)
    upload = models.FileField(upload_to='audios', validators=[audio_validator])
    device = models.TextField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.upload.name


class Zip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=100, blank=True, null=True)
    upload = models.FileField(upload_to='zips', validators=[zip_validator])
    device = models.TextField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.upload.name


class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=100, blank=True, null=True)
    upload = models.FileField(upload_to='picture/%Y/%m/%d', validators=[picture_validator])
    device = models.TextField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.upload.name
