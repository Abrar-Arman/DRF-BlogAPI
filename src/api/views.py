from django.shortcuts import render
from rest_framework import generics
from .models import Blogs,Comments
from .serilizers import BlogsSerilizer,CommentsSerilizer,BlogsDetailSerilizer,CommentUpdateSerilizer
from .pagination import BlogListPagination
from .commen.base_views import BaseCreateView
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
class BlogListCreate(BaseCreateView,generics.ListAPIView):
    msg='Blog added successfully'
    queryset=Blogs.objects.all()
    serializer_class=BlogsSerilizer
    pagination_class=BlogListPagination
    parser_classes = (MultiPartParser, FormParser)

class BlogRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blogs.objects.all()
    serializer_class=BlogsDetailSerilizer
    lookup_field='pk'

class CommentsCreate(BaseCreateView,):
    msg = "Comment added successfully"
    queryset=Comments.objects.all()
    serializer_class=CommentsSerilizer

class CommentsRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
     queryset=Comments.objects.all()
     serializer_class=CommentUpdateSerilizer
     lookup_field='pk'
