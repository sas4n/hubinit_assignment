from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer