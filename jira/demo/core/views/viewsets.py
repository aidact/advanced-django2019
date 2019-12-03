import logging

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from auth_.models import MainUser

from core.models import (Project,
                         Block,
                         Task,
                         TaskDocument)
from core.serializers import (ProjectSerializer,
                              BlockSerializer,
                              TaskSerializer,
                              TaskDocumentSerializer,
                              TaskDocumentFullSerializer,
                              TaskDocumentShortSerializer)

logger = logging.getLogger(__name__)


class ProjectViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Project.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        return serializer.save(name=self.request.data['name'],
                               description=self.request.data['description'],
                               creator=self.request.user)

    def get_queryset(self):
        queryset = self.queryset.filter(creator=self.request.user)
        return queryset

    @action(methods=['GET'], detail=True)
    def blocks(self, request, pk):
        return Block.objects.get(project_id=pk)


class BlockViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Block.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BlockSerializer

    def perform_create(self, serializer):
        return serializer.save(name=self.request.data['name'],
                               type=self.request.data['type'],
                               project=Project.objects.get(id=self.request.data['project']))

    def get_queryset(self):
        return self.queryset.all()

    @action(methods=['GET'], detail=True)
    def tasks(self, request, pk):
        tasks = Task.objects.filter(block_id=pk)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(name=self.request.data['name'],
                        description=self.request.data['description'],
                        block=Block.objects.get(id=self.request.data['block']),
                        executor=MainUser.objects.get(id=self.request.data['executor']),
                        order=self.request.data['order'])
        logger.info(f"{self.request.user} created task: {serializer.data.get('name')}")

    def get_queryset(self):
        return self.queryset.all()


class TaskDocumentViewSet(viewsets.ModelViewSet):
    serializer_class = TaskDocumentSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    queryset = TaskDocument.objects.all()

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskDocumentFullSerializer
        return TaskDocumentShortSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
