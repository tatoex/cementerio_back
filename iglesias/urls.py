from rest_framework.routers import DefaultRouter
from .viewsets import ParroquiaViewSet, ParroquiaReadViewSet, IglesiaViewSet, IglesiaReadViewSet, LinkRedSocialViewSet, LinkRedSocialReadViewSet
router=DefaultRouter()

router.register(r'parroquia',ParroquiaViewSet, basename='parroquia')
router.register(r'parroquiaread',ParroquiaReadViewSet, basename='parroquiaread')
router.register(r'iglesia',IglesiaViewSet, basename='iglesia')
router.register(r'iglesiaread',IglesiaReadViewSet, basename='iglesiaread')
router.register(r'social',LinkRedSocialViewSet, basename='social')
router.register(r'socialread',LinkRedSocialReadViewSet, basename='socialread')

urlpatterns = router.urls
