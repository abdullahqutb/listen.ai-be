from django.contrib import admin
from .models import PDFFile, AudioFile

# Register your models here.
admin.site.register(PDFFile)
admin.site.register(AudioFile)
