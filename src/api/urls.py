from django.urls import path
from .views import BlogListCreate,BlogRetriveUpdateDestroy,CommentsCreate,CommentsRetriveUpdateDestroy
urlpatterns = [
    path('blogs/',BlogListCreate.as_view()),
    path('blog/<int:pk>/',BlogRetriveUpdateDestroy.as_view()),
    path('comments/',CommentsCreate.as_view()),
    path('comment/<int:pk>/',CommentsRetriveUpdateDestroy.as_view()),
]
