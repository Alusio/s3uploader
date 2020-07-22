from django.contrib import admin

from uploader.models import Document, Audio, Video, Zip, Picture

# Register your models here.
admin.site.register(Document)
admin.site.register(Audio)
admin.site.register(Video)
admin.site.register(Zip)
admin.site.register(Picture)
