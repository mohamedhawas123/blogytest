from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from account.models import Account
from blog.models import BlogPost
from blog.api.serializers import BlogpostSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def api_detail_blog_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogpostSerializer(blog_post)
        return Response(serializer.data)


@api_view(['PUT'])
def api_update_blog_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BlogpostSerializer(blog_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "update successful"
            return Response(data=data)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def api_delete_blog_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = blog_post.delete()
        data = {}
        if operation:
            data['success'] = "delete successful"
        else:
            data['filure'] = "delete faild"

        return Response(data=data)


@api_view(['POST', ])
def api_create_blog_view(request):

    account = Account.objects.get(pk=1)
    blog_post = BlogPost(author=account)

    if request.method == "POST":
        serializer = BlogpostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiBlogPost(ListAPIView):
    queryset = BlogPost.objects.all()
    serilzer_class = BlogpostSerializer
    Athentication_class = (TokenAuthentication)
