from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from course.api.serializers.comment_serializer import CommentSerializer
from course.api.serializers.comment_serializer import CourseCommentSerializer
from course.api.models.comments_model import CourseComment
from rest_framework.exceptions import NotFound


class CourseCommentView(ModelViewSet):
    queryset = CourseComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]

    def list(self, request):
        serializer = CommentSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        comment = get_object_or_404(self.queryset, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        request.data['created_by'] = request.user.id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        comment = get_object_or_404(self.queryset, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        comment = get_object_or_404(self.queryset, pk=pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        comment = get_object_or_404(self.queryset, pk=pk)
        comment.delete()
        return Response({"message": "comment deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['GET'], url_name='get-a-course-comment')
    def get_a_course_comments(self, request, *args, **kwargs):
        if request.GET.get('course_id'):
            try:
                all_comments_of_a_course = CourseComment.objects.filter(course_id=request.GET.get('course_id'))
            except CourseComment.DoesNotExist:
                return NotFound("the course doesn't have any comment")
            serializer = CourseCommentSerializer(all_comments_of_a_course, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("The course id params not provided!!", status=status.HTTP_406_NOT_ACCEPTABLE)