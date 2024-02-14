from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from instagram.models import Post


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class PostSerializer(ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
