from django.urls import path
from .views import FileUploadView

urlpatterns = [
    path('upload_pdf/', FileUploadView.as_view(), name='upload_pdf'),
    # path('audio/', AudioFileView.as_view(), name='audio_file'),
]