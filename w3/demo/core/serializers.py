from rest_framework import serializers

from core.models import Project, Task, Block, TaskDocument, TaskComment


class ProjectSerializer(serializers.ModelSerializer):
    creator_name = serializers.SerializerMethodField()
    creator_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'creator',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'creator', 'executor', 'block', 'order')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('id', 'name', 'type', 'project')

    project = ProjectSerializer()


class TaskDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDocument
        fields = ('id', 'document', 'creator', 'task')

    task = TaskSerializer()


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('id', 'body', 'creator', 'created_at', 'task')

    task = TaskSerializer()
