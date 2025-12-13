from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogListCreate.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', views.BlogRetrieveUpdateDestroy.as_view(), name='blog-detail'),
    path('comments/', views.CommentsCreate.as_view(), name='comment-create'),
    path('comments/<int:pk>/', views.CommentsRetrieveUpdateDestroy.as_view(), name='comment-detail'),  # Fixed!
]
