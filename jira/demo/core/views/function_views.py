from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Comment, Task
from core.serializers import CommentSerializer


@api_view(['POST'])
def create_comment(request):
    comment = Comment.objects.create(
        content=request.data['content'],
        task=Task.objects.get(id=request.data['task']),
        creator=request.user)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)


@api_view(['GET'])
def get_comments(request):
    queryset = Comment.objects.all()
    serializer = CommentSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_comment_by_task(request):
    task_id = request.query_params.get('task')
    comments = Comment.objects.get(task_id=task_id)
    serializer = CommentSerializer(comments)
    return Response(serializer.data)
