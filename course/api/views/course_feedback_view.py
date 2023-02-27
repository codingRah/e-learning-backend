from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from course.api.serializers.course_feedback_serializer import CourseFeedbackSerializer
from course.api.models.course_feedback import CourseFeedback
from rest_framework.response import Response


class CourseFeedbackView(APIView):
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        """Return an instance this."""
        try: 
            return CourseFeedback.objects.get(pk=pk)
        except CourseFeedback.DoesNotExist:
            return Response('The attachment Not found!', status=status.HTTP_404_NOT_FOUND) 
    
    def get(self, request):
        attachment = CourseFeedback.objects.all()
        serializer = CourseFeedbackSerializer(attachment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data['user'] = request.user.id
        serializer = CourseFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        attachment = self.get_object(pk=pk)
        serializer = CourseFeedbackSerializer(data=request.data, instance=attachment)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        attachment = self.get_object(pk=pk)
        serializer = CourseFeedbackSerializer(data=request.data, instance=attachment, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        attachment = self.get_object(pk=pk)
        attachment.delete()
        return Response({'message:', 'The feedback deleted successfully'}, status=status.HTTP_204_NO_CONTENT)