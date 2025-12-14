from adrf.serializers import ModelSerializer as AsyncModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comments, Blogs


class UserSerilizer(AsyncModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class CommentsSerilizer(AsyncModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class CommentUpdateSerilizer(AsyncModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'author', 'blog']


class BlogsSerilizer(AsyncModelSerializer):
    author = UserSerilizer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='author' 
    )
    
    class Meta:
        model = Blogs
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class BlogsDetailSerilizer(AsyncModelSerializer):
    comments = CommentsSerilizer(many=True, read_only=True)
    author = UserSerilizer(read_only=True)

    class Meta:
        model = Blogs
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


