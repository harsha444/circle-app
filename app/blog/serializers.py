from rest_framework import serializers
from blog import models


class BlogSerializer(serializers.ModelSerializer):
    """Serializer for Blog Model"""

    class Meta:
        model = models.Blog
        fields = ('id', 'heading', 'text')

    def create(self, validated_data):
        blog = models.Blog.objects.create(
            heading=validated_data['heading'],
            text=validated_data['text']
        )

        return blog


class UserBlogCommentSerializer(serializers.ModelSerializer):
    """Serializer for UserBlogComment Model"""

    class Meta:
        model = models.UserBlogComment
        fields = ('id', 'blog_id', 'user_id')

    def create(self, validated_data):
        user_blog_comment = models.UserBlogComment.objects.create(
            user_id=validated_data['user_id'],
            blog_id=validated_data['blog_id'],
            comment=validated_data.get('comment')
        )

        return user_blog_comment
