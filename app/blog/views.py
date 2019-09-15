from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from blog import serializers
from blog import models
from users import serializers as user_serializers
from users.models import UserProfile
from django.http import Http404


class BlogViewSet(viewsets.ModelViewSet):
    """Handles creating/updating a Blog"""
    serializer_class = serializers.BlogSerializer
    queryset = models.Blog.objects.all()


class CommonBlog(APIView):
    """Gets the common blogs for given blog's first level friends"""

    @staticmethod
    def get_blog_object(pk):
        try:
            return models.Blog.objects.get(pk=pk)
        except models.Blog.DoesNotExist:
            raise Http404

    @staticmethod
    def get_blog_user_comments(pk):
        return list(models.UserBlogComment.objects.filter(blog_id=pk).values_list('user', flat=True).distinct())

    @staticmethod
    def get_first_level_friends_comment_blogs(user_ids):
        user_commented_blogs = list(
            models.UserBlogComment.objects.filter(user_id__in=user_ids).values_list('blog', flat=True))
        return user_commented_blogs

    def get(self, request, pk, format=None):
        blog_commented_users = CommonBlog.get_blog_user_comments(pk)
        first_level_friends_blogs = CommonBlog.get_first_level_friends_comment_blogs(blog_commented_users)
        blogs = models.Blog.objects.filter(id__in=first_level_friends_blogs)
        blog_serializer = serializers.BlogSerializer(blogs, many=True)
        # queryset = models.Blog.objects.filter(pk__in=blog_ids_required)
        return Response(blog_serializer.data)
