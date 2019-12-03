from django.urls import path
from rest_framework.routers import DefaultRouter

from core.views.viewsets import ProjectViewSet, BlockViewSet, TaskDocumentViewSet, TaskViewSet
from core.views import function_views

urlpatterns = [
    path('comments/create/', function_views.create_comment),
    path('comments/', function_views.get_comments),
    path('comments_by_task/', function_views.get_comment_by_task),
]

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, base_name='core')
router.register(r'blocks', BlockViewSet, base_name='core')
router.register(r'documents', TaskDocumentViewSet, base_name='core')
router.register(r'tasks', TaskViewSet, base_name='core')

urlpatterns += router.urls
