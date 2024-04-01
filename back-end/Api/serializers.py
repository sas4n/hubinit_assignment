from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class BlogSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author_name.username', read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'blog_title', 'author_name', 'blog_text', 'blog_status']