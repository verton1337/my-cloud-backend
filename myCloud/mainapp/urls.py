from django.urls import path, include
from mainapp.views import MainView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', MainView, basename='api')
urlpatterns = router.urls


