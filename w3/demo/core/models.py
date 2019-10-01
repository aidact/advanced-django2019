from django.db import models

from auth_.models import User
from utils.constants import TYPES, NEW


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f'{self.name}: {self.creator}'


class Block(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPES, default=NEW)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.project}'


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    executor = models.ForeignKey(User, related_name='executor', on_delete=models.CASCADE)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    order = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}: {self.creator}, {self.block}'


class TaskDocument(models.Model):
    document = models.FileField(upload_to='files/')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.document}: {self.creator}'


class TaskComment(models.Model):
    body = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.creator}: {self.task}'
