from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Reaction(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reactions")

    reaction_type = models.CharField(max_length=20)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="reactions"
    )

    def __str__(self):
        return self.reaction_type
