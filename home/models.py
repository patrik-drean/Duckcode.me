from django.db import models
from django.contrib.auth.models import User

class User(User):
    pass

class Blog(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    filename = models.TextField(blank=True, null=True)
    alt_text = models.TextField(blank=True, null=True)
    top_post = models.BooleanField()

    def image_url(self):
        blog = Blog.objects.get(id = self.id)
        url = '/home/media/blog_main/' + blog.filename
        return url

class Category(models.Model):
    name = models.TextField()
    filename = models.TextField(blank=True, null=True)

    def image_url(self):
        category = Category.objects.get(id = self.id)
        url = '/home/media/blog_main/' + category.filename
        return url
