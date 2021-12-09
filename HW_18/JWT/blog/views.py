from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import PostSerializer, CommentSerializer, CategorySerializers, PostCreateSerializer, \
    PostDetailSerializer, PostUpdateSerializer
from .models import Post, Comment, Category
from rest_framework import status


@api_view()
@permission_classes([IsAuthenticated])
def posts(request):
    posts = Post.objects.all()
    ser_data = PostSerializer(posts, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)

@api_view()
@permission_classes([IsAuthenticated])
def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response({'error': 'this post does not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = PostSerializer(post)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated])
def comments(request):
    comments = Comment.objects.all()
    ser_data = CommentSerializer(comments, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated])
def comment(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        return Response({'error': 'this comment does not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = CommentSerializer(comment)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated])
def categories(request):
    category = Category.objects.all()
    ser_data = CategorySerializers(category, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAuthenticated])
def category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response({'error': 'this category does not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = CategorySerializers(category)
    return Response(ser_data.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_create(request):
    info = PostCreateSerializer(data=request.data)
    if info.is_valid():
        info.save()
        return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def post_create_detail_update_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "GET":
        ser_data = PostDetailSerializer(post)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


    elif request.method == 'PUT':
        if post.user != request.user:
            return Response(data={'msg': 'this post owned by another user'}, status=status.HTTP_400_BAD_REQUEST)

        ser_data = PostUpdateSerializer(post, data=request.data)
        ser_data.is_valid(raise_exception=True)
        updated_post = ser_data.save()
        resp_serializer = PostDetailSerializer(updated_post)
        return Response(resp_serializer.data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        if post.user != request.user:
            return Response(data={'msg': 'this post owned by another user'}, status=status.HTTP_400_BAD_REQUEST)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



