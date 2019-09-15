from django.db import models
from users.models import UserProfile


class Blog(models.Model):
    """Blog model for storing blogs"""
    heading = models.CharField(max_length=255, null=False)
    text = models.TextField(null=True, blank=True)


class UserBlogComment(models.Model):
    """UserBlogComment model to keep track of user comments on blogs"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
