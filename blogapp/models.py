from django.db import models
from django.contrib.auth.models import User


class Article (models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, related_name='articles')


def __str__(self):
    return self.title

    # STATUS_CHOICES = (
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    # )
# tag = models.CharField(max_length=100)
# link = models.CharField(max_length=100)
# code_snippet = models.FilePathField(path="/img")
# slug = models.SlugField(null=True, unique_for_date='publish')
# publish = models.DateTimeField()
# created = models.DateTimeField(auto_now_add=True)
# updated = models.DateTimeField(auto_now=True)
# status = models.CharField(
#     max_length=10, choices=STATUS_CHOICES, default='draft')


# to sort published articles in descending order
# class Meta:
#     ordering = ('-publish',)


class Comment (models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# render body with limitation of 50 signs
# def snippet(self):
#     return self.body[:50]+"..."
