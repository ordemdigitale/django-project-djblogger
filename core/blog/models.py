import uuid

from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
    """
    Holds posts data
    """

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default="draft")
    tags = TaggableManager()
    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
