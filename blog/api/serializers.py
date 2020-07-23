from rest_framework import serializers
from blog.models import BlogPost


class BlogpostSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('SOMEFUCNTIO')

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'date_updated']


def SOMEFUCNTIO(slef, blog_post):
    username = blog_post.author.username
    return username
