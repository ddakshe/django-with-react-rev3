from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer


# class PublicPostListView(ListAPIView):
#     queryset = Post.objects.all().filter(is_public=True)
#     serializer_class = PostSerializer

class PublicPostListView(APIView):
    def get(self, request):
        qs = Post.objects.filter(is_public=True)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)


public_list_view = PublicPostListView.as_view()


# @api_view(['GET'])
# def public_list_view(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        print('request.body', request.body)
        print('request.POST', request.POST)
        return super().dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            self.permission_classes = [IsAuthenticated, ]
            self.check_permissions(request)
        return super().create(request, *args, **kwargs)
