from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer, CommentSerializer, CategorySerializers
from .models import Post, Comment, Category


@api_view()
def posts(request):
    posts = Post.objects.all()
    ser_data = PostSerializer(posts, many=True)
    return Response(ser_data.data)

@api_view()
def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response({'error': 'this post does not exist'})
    ser_data = PostSerializer(post)
    return Response(ser_data.data)


@api_view()
def comments(request):
    comments = Comment.objects.all()
    ser_data = CommentSerializer(comments, many=True)
    return Response(ser_data.data)


@api_view()
def comment(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        return Response({'error': 'this comment does not exist'})
    ser_data = CommentSerializer(comment)
    return Response(ser_data.data)


@api_view()
def categories(request):
    category = Category.objects.all()
    ser_data = CategorySerializers(category, many=True)
    return Response(ser_data.data)


@api_view()
def category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response({'error': 'this category does not exist'})
    ser_data = CategorySerializers(category)
    return Response(ser_data.data)