from rest_framework import serializers
from .models import Post, Comment, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'user', 'body', 'created', 'updated', 'status')
        # extra_kwargs = {
        #     'slug':{'write_only': True,},
        # }


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'title', 'description', 'post', 'created', 'updated')


class CategorySerializers(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'posts')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'user')


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'user', 'body', 'created', 'updated', 'status')
        # extra_kwargs = {
        #     'slug':{'write_only': True,},
        # }


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'user')