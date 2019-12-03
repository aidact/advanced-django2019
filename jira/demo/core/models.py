from django.db import models

from auth_.models import MainUser
from utils.constants import TYPES, NEW
from utils.upload import task_document_path
from utils.validators import task_document_size, task_document_extension


class ProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class BlockManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='projects')

    objects = ProjectManager()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f'{self.name}: {self.creator}'


class Block(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPES, default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    objects = BlockManager()

    def __str__(self):
        return f'{self.name}: {self.project}'


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    creator = models.ForeignKey(MainUser, related_name='creator', on_delete=models.CASCADE, null=True)
    executor = models.ForeignKey(MainUser, related_name='executor', on_delete=models.CASCADE, null=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    order = models.CharField(max_length=100)

    objects = TaskManager()

    def __str__(self):
        return f'{self.name}: {self.creator}, {self.block}'


class TaskDocument(models.Model):
    document = models.FileField(upload_to=task_document_path, validators=[task_document_size, task_document_extension],
                                null=True)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.document}: {self.creator}'

class Comment(models.Model):
    content = models.CharField(max_length=255)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='comment')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return f'{self.creator}: {self.task}'
