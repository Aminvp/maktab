from rest_framework import serializers
from .models import Post, Comment, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'user', 'body', 'created', 'updated', 'status')
        extra_kwargs = {
            'slug': {'write_only': True, },
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'title', 'description', 'post', 'created', 'updated')


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'post')
