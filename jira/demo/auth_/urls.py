from rest_framework import routers

from auth_.views import MainUserViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', MainUserViewSet, base_name='auth_')
router.register(r'profiles', ProfileViewSet, base_name='profiles')

urlpatterns = router.urls

