from django.shortcuts import render
from rest_framework import generics
from .models import Blogs,Comments
from .serilizers import BlogsSerilizer,CommentsSerilizer,BlogsDetailSerilizer,CommentUpdateSerilizer
# Create your views here.
class BlogListCreate(generics.ListCreateAPIView):
    queryset=Blogs.objects.all()
    serializer_class=BlogsSerilizer

class BlogRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blogs.objects.all()
    serializer_class=BlogsDetailSerilizer
    lookup_field='pk'

class CommentsCreate(generics.CreateAPIView):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerilizer

class CommentsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
     queryset=Comments.objects.all()
     serializer_class=CommentUpdateSerilizer
     lookup_field='pk'
