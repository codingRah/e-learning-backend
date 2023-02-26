from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from course.api.serializers.course_attachment_serializer import AttachmentSerializer
from course.api.models.course_attachment_model import CourseAttachment
from course.api.models.course_model import Course
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from datetime import datetime
from django.conf import settings
import os


class AttachmentView(APIView):
    # permission_classes = (IsAuthenticated, )

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
        course_id = request.GET.get('course_id')
        if not course_id:
            raise NotFound("Course ID params not provided!")
        course = Course.objects.get(pk=int(course_id))
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            handle_uploaded_file(uploaded_file, course.files)
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
    
    def patch(self, request, pk):
        attachment = self.get_object(pk=pk)
        serializer = AttachmentSerializer(data=request.data, instance=attachment, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        attachment = self.get_object(pk=pk)
        course_id = request.GET.get('course_id')
        # if not course_id:
        #     raise NotFound("Course id params not provided!")
        # if delete_an_attachment(Course.objects.get(pk=int(course_id)), attachment.name):
        attachment.delete()
        return Response({'message:', 'The attachment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        # else: 
        #     return Response({'message': 'the attchment already deleted'}, status=status.HTTP_204_NO_CONTENT)
    
def handle_uploaded_file(f, directory):
    with open(os.path.join(os.path.join(os.path.join(settings.MEDIA_ROOT, directory), 'attachments'), f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def delete_an_attachment(course, attachment_name):
    if os.path.exists(os.path.join(os.path.join(settings.MEDIA_ROOT, str(course.files) + '/attachments'), str(attachment_name))):
        os.remove(os.path.join(os.path.join(os.path.join(settings.MEDIA_ROOT, str(course.files)), 'attachments'), str(attachment_name)))
        return True
    else:
        return False