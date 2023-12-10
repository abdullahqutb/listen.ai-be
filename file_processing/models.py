# file_processing/models.py

from django.db import models
from django.contrib.auth.models import User

class PDFFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pdf_files', default="abu@gmail.com")
    file_url = models.URLField(max_length=1024, null=True)  # URL to the PDF file on S3
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PDF File uploaded by {self.user.username}"

class AudioFile(models.Model):
    related_pdf = models.ForeignKey(PDFFile, on_delete=models.CASCADE, related_name='audio_files')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audio_files', default="abu@gmail.com")
    file_url = models.URLField(max_length=1024, null=True)  # URL to the audio file on S3
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audio File related to {self.related_pdf} and uploaded by {self.user.username}"
