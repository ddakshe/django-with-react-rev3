from django.urls import include, path
from rest_framework.routers import DefaultRouter


from instagram.views import PostViewSet, PublicPostListView

app_name = 'instagram'

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('public/', PublicPostListView.as_view(), name='post_list'),
    path('', include(router.urls)),
]
