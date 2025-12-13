from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comments,Blogs


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

class CommentsSerilizer(serializers.ModelSerializer):
   
   class Meta:
        model=Comments
        fields='__all__'
        read_only_fields = ['id','created_at', 'updated_at']

class CommentUpdateSerilizer(serializers.ModelSerializer):
    class Meta:
          model=Comments
          fields='__all__'
          read_only_fields = ['id','created_at', 'updated_at','author','blog']

class BlogsSerilizer(serializers.ModelSerializer):
    author = UserSerilizer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='author' 
    )
    class Meta:
        model=Blogs
        fields='__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

class BlogsDetailSerilizer(serializers.ModelSerializer):
    comments=CommentsSerilizer(many=True, read_only=True)
    author = UserSerilizer(read_only=True)

    class Meta:
        model=Blogs
        fields='__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']



