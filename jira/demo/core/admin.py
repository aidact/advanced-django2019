from django.contrib import admin

from core.models import Project, Task, Block, TaskDocument, Comment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creator')
    fields = (
        'name',
        'description',
        'creator'
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creator', 'executor', 'block', 'order')
    fields = (
        'name',
        'description',
        'creator',
        'executor',
        'block',
        'order'
    )


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'project')
    fields = (
        'name',
        'type',
        'project'
    )


@admin.register(TaskDocument)
class TaskDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'document', 'creator', 'task')
    fields = (
        'document',
        'creator',
        'task'
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'creator', 'task')
    fields = (
        'content',
        'creator',
        'task'
    )

