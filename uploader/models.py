from django.contrib.auth.models import User
from django.db import models


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()
    device = models.TextField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.upload.name
