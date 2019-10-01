from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import (Project,
                         Block,
                         Task,
                         TaskDocument,
                         TaskComment)
from core.serializers import (ProjectSerializer,
                              BlockSerializer,
                              TaskSerializer,
                              TaskCommentSerializer,
                              TaskDocumentSerializer)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(creator=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=self.request.user)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        try:
            project = get_object_or_404(queryset, pk=pk)
        except Project.DoesNotExist:
            raise Http404
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class BlockViewSet(viewsets.ViewSet):
    queryset = Block.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BlockSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_queryset(self):
        return self.queryset.all()


class TaskViewSet(viewsets.ViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


class TaskDocumentViewSet(viewsets.ViewSet):
    queryset = TaskDocument.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskDocumentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=self.request.user)
        return Response(serializer.data)

    def get_queryset(self):
        return self.queryset.all()


class TaskCommentViewSet(viewsets.ViewSet):
    queryset = TaskComment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskCommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=self.request.user, created_at=timezone.now())
        return Response(serializer.data)

    def get_queryset(self):
        return self.queryset.all()
