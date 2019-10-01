from rest_framework.routers import DefaultRouter

from core.views import ProjectViewSet, BlockViewSet, TaskViewSet, TaskCommentViewSet, TaskDocumentViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, base_name='core')
router.register(r'blocks', BlockViewSet, base_name='core')
router.register(r'tasks', TaskViewSet, base_name='core')
router.register(r'tasks/documents', TaskDocumentViewSet, base_name='core')
router.register(r'tasks/comments', TaskCommentViewSet, base_name='core')
urlpatterns = router.urls
