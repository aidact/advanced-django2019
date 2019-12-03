import os
import shutil


def task_document_path(instance, filename):
    task_id = instance.task_id
    return f'tasks/{task_id}/{filename}'


def task_delete_path(document):
    datetime_path = os.path.abspath(os.path.join(document.path, '..'))
    shutil.rmtree(datetime_path)