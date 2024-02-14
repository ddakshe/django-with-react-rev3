from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer


class PublicPostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        print('request.body', request.body)
        print('request.POST', request.POST)
        return super().dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            self.permission_classes = [IsAuthenticated,]
            self.check_permissions(request)
        return super().create(request, *args, **kwargs)