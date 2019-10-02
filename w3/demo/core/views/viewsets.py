from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import (Project,
                         Block)
from core.serializers import (ProjectSerializer,
                              BlockSerializer)


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
                               project_id=self.request.data['project_id'])

    def get_queryset(self):
        return self.queryset.all()
