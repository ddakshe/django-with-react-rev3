from django.urls import include, path
from rest_framework.routers import DefaultRouter

from instagram.views import PostViewSet

app_name = 'instagram'

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
