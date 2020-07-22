from django.contrib.auth.models import User
from django.db import models


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()

    def __str__(self):
        return self.upload.name
