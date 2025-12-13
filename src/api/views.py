# -----------------------------
# imports
# -----------------------------
from adrf.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Blogs, Comments
from .serilizers import (
    BlogsSerilizer,
    BlogsDetailSerilizer,
    CommentsSerilizer,
    CommentUpdateSerilizer,
)
from .pagination import BlogListPagination
from .commen.base_views import BaseCreateView


class BlogListCreate(ListCreateAPIView, BaseCreateView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerilizer
    pagination_class = BlogListPagination
    parser_classes = (MultiPartParser, FormParser)
    msg = "Blog added successfully"
    


class BlogRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsDetailSerilizer
    lookup_field = "pk"


class CommentsCreate(CreateAPIView, BaseCreateView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerilizer
    msg = "Comment added successfully"


class CommentsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentUpdateSerilizer
    lookup_field = "pk"



