# -----------------------------
# imports
# -----------------------------
from adrf.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView
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
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .commen.base_views import BaseCreateView
from .permissions import IsOwnerOrReadOnlyPermission


class BlogListCreate(BaseCreateView,ListAPIView,CreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerilizer
    pagination_class = BlogListPagination
    parser_classes = (MultiPartParser, FormParser)
    permission_classes=(IsAuthenticatedOrReadOnly,)
    msg = "Blog added successfully"
    


class BlogRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsDetailSerilizer
    lookup_field = "pk"
    permission_classes=[IsOwnerOrReadOnlyPermission]


class CommentsCreate(BaseCreateView,ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerilizer
    msg = "Comment added successfully"


class CommentsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentUpdateSerilizer
    lookup_field = "pk"



