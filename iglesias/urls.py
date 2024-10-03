from rest_framework.routers import DefaultRouter
from .viewsets import ParroquiaViewSet, IglesiaViewSet, LinkRedSocialViewSet
router=DefaultRouter()

router.register(r'parroquia',ParroquiaViewSet, basename='parroquia')
router.register(r'iglesia',IglesiaViewSet, basename='iglesia')
router.register(r'social',LinkRedSocialViewSet, basename='social')

urlpatterns = router.urls
