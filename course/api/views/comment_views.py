from rest_framework.decorators import permission_classes , api_view
from rest_framework.response import Response
from rest_framework import status
from course.api.serializers.comment_serializer import CommentSerializer
from course.api.models.comments_model import CourseComment

@api_view(['GET', 'POST'])
def course_comment_list_create_views(request):

    if request.method == 'GET':
        comment = CourseComment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def course_comment_update_delete_views(request,pk):

    if request.method == 'GET':
        comment = CourseComment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    if request.method == 'PUT':
        comment = CourseComment.objects.get(pk=pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        comment = CourseComment.objects.get(pk=pk)
        comment.delete()
        return Response({'message:' 'comment delete successfully'}, status=status.HTTP_204_NO_CONTENT)
    

