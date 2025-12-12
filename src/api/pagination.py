from rest_framework.pagination import CursorPagination

class BlogListPagination(CursorPagination):
    page_size = 15
    ordering = 'id' 