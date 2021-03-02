from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('blog-article-detail', args=(str(self.id)))
        return reverse('blog-home')


class Post(models.Model):
    title = models.CharField(max_length=20)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    category = models.CharField(max_length=20, default='uncategorized')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('blog-article-detail', args=(str(self.id)))
        return reverse('blog-home')

