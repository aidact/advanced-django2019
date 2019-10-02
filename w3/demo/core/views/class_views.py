from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Task, TaskComment, TaskDocument
from core.serializers import TaskSerializer, TaskCommentSerializer, TaskDocumentSerializer


class TaskAPIView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(creator_id=request.user.id, block_id=request.query_params['block_id'])
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(request)
        return Response(serializer.data)


class TaskCommentAPIView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = TaskComment.objects.filter(creator_id=request.user.id)
        serializer = TaskCommentSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(request)
        return Response(serializer.data)


class TaskDocumentAPIView(APIView):
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = TaskDocument.objects.filter(creator_id=request.user.id)
        serializer = TaskDocumentSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskDocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(request)
        return Response(serializer.data)
