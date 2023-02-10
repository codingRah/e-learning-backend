from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from course.api.serializers.course_attachment_serializer import AttachmentSerializer
from course.api.models.course_attachment_model import CourseAttachment
from rest_framework.response import Response


def attachment_list_create_views(request):

    if request.method == 'GET':
        attachment = CourseAttachment.objects.all()
        serializer = AttachmentSerializer(attachment, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


def attachment_update_delete_views(request, pk):

    if request.method == 'GET':
        attachment = CourseAttachment.objects.get(pk=pk)
        serializer = AttachmentSerializer(attachment, many=True)
        return Response(serializer.data)
    

    if request.method == 'PUT':
        attachment = CourseAttachment.objects.get(pk=pk)
        serializer = AttachmentSerializer(data=request.data, instance=attachment)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'DELETE':
        attachment = CourseAttachment.objects.get(pk=pk)
        attachment.delete()
        return Response({'message:', 'the couser attachment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)