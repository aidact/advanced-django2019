from rest_framework import serializers

from core.models import Project, Task, Block, TaskDocument, TaskComment
from auth_.serializers import UserSerializer
from auth_.models import User


class ProjectSerializer(serializers.ModelSerializer):
    # creator = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('creator',)


class BlockSerializer(serializers.ModelSerializer):
    # project = ProjectSerializer()

    class Meta:
        model = Block
        fields = '__all__'
        read_only_fields = ('project',)


class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    executor = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())
    block = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all())
    order = serializers.CharField(max_length=100)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('creator',)

    def create(self, request):
        Task.objects.create(name=self.validated_data['name'],
                            description=self.validated_data['description'],
                            creator=request.user,
                            executor=self.validated_data['executor'],
                            block=self.validated_data['block'],
                            order=self.validated_data['order'])


class TaskDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDocument
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):
    body = serializers.CharField(max_length=100)
    created_at = serializers.DateField()
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

    class Meta:
        model = TaskComment
        fields = '__all__'
        read_only_fields = ('creator',)

    def create(self, request):
        TaskComment.objects.create(body=self.validated_data['body'],
                                   creator=request.user,
                                   created_at=self.validated_data['created_at'],
                                   task=self.validated_data['task'])
