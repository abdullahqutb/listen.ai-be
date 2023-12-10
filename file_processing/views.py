from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
# file_processing/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PDFFile
from .utils import upload_to_s3
# ... other imports ...

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        user = request.user

        if file and file.name.endswith('.pdf'):
            # Assuming 'file_processing/upload_to_s3' is your upload function
            file_url = upload_to_s3(file, f"pdfs/{user.id}/{file.name}")
            
            PDFFile.objects.create(user=user, file_url=file_url)
            return Response({'file_url': file_url}, status=201)

        return Response({'message': 'Invalid file format'}, status=400)


# class AudioFileView(APIView):
#     # View to retrieve or process audio files
