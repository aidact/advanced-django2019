from rest_framework.routers import DefaultRouter
from django.urls import path

from core.views.viewsets import ProjectViewSet, BlockViewSet
from core.views.class_views import TaskAPIView, TaskCommentAPIView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, base_name='core')
router.register(r'blocks', BlockViewSet, base_name='core')

urlpatterns = [
    path('tasks/', TaskAPIView.as_view()),
    path('tasks/comment/', TaskCommentAPIView.as_view())

] + router.urls

