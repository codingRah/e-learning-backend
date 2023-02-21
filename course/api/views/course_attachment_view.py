from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from course.api.serializers.course_attachment_serializer import AttachmentSerializer
from course.api.models.course_attachment_model import CourseAttachment
from rest_framework.response import Response
from datetime import datetime


class AttachmentView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        """Return an instance this."""
        try: 
            return CourseAttachment.objects.get(pk=pk)
        except CourseAttachment.DoesNotExist:
            return Response('The attachment Not found!', status=status.HTTP_404_NOT_FOUND) 
    
    def get(self, request):
        attachment = CourseAttachment.objects.all()
        serializer = AttachmentSerializer(attachment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        uploaded_file = request.FILES['name']
        extension = uploaded_file.name.split('.')[-1]
        request.data['file_type'] = extension
        request.data['file_size'] = uploaded_file.size
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            #uploading file is not implemented!
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        attachment = self.get_object(pk=pk)
        serializer = AttachmentSerializer(data=request.data, instance=attachment)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        attachment = self.get_object(pk=pk)
        serializer = AttachmentSerializer(data=request.data, instance=attachment, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        attachment = self.get_object(pk=pk)
        attachment.delete()
        return Response({'message:', 'The attachment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
def handle_uploaded_file(f, course_name, username):
    extension = f.name.split('.')[-1]
    with open(f'Attachments/{course_name}-{username}/{f.name}-{datetime.now()}.{extension}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)