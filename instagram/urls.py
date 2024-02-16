from django.urls import include, path
from rest_framework.routers import DefaultRouter

from instagram import views

app_name = 'instagram'

router = DefaultRouter()
router.register('post', views.PostViewSet, basename='post')

urlpatterns = [
    # path('public/', PublicPostListView.as_view(), name='post_list'),
    path('public/', views.public_list_view, name='post_list'),
    path('', include(router.urls)),
]
