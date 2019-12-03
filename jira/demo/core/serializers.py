from rest_framework import serializers

from auth_.serializers import MainUserSerializer
from core.models import Project, Task, Block, TaskDocument, Comment
# from utils.constants import TYPES
from utils.validators import comment_length

TYPES = ['TO_DO', 'IN_PROGRESS', 'DONE', 'NEW']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('creator',)


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'

    def validate_type(self, value):
        if value in TYPES:
            return value
        raise serializers.ValidationError('Not valid type')


# class TaskSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=255)
#     executor = serializers.PrimaryKeyRelatedField(required=False, queryset=MainUser.objects.all(), allow_null=True)
#     block = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all())
#     order = serializers.CharField(max_length=100)
#
#     optional_fields = ['description']
#
#     class Meta:
#         model = Task
#         fields = '__all__'
#         read_only_fields = ('creator',)
#
#     def create(self, request):
#         task = Task.objects.create(name=self.validated_data['name'],
#                                    description=self.validated_data['description'],
#                                    creator=request.user,
#                                    executor=self.validated_data['executor'],
#                                    block=self.validated_data['block'],
#                                    order=self.validated_data['order'])
#         return task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDocument
        fields = '__all__'


class TaskDocumentShortSerializer(serializers.ModelSerializer):
    creator = MainUserSerializer(read_only=True)
    # document = serializers.FileField(write_only=True)
    # document_url = serializers.SerializerMethodField(read_only=True)
    read_only_fields = ('task',)

    class Meta:
        model = TaskDocument
        fields = ('id', 'document', 'creator', 'task')

    def get_document_url(self, obj):
        if obj.document:
            return self.context['request'].build_absolute_uri(obj.document.url)
        return None


class TaskDocumentFullSerializer(TaskDocumentShortSerializer):
    class Meta(TaskDocumentShortSerializer.Meta):
        fields = TaskDocumentShortSerializer.Meta.fields + ('priority', 'description')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('creator', )

    def validate_content(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Too long comment')
        return value


class CommentGetSerializer(CommentSerializer):
    task = TaskSerializer()
    creator = MainUserSerializer()

    class Meta(CommentSerializer.Meta):
        fields = CommentSerializer.Meta.fields


