from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Blog(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    filename = models.TextField(blank=True, null=True)

    def image_url(self):
        ''' Always return an image '''
        product = Blog.objects.get(id = self.id).
        if product is not None:
            url = '/static/catalog/media/products/' + product.Filename
        return url

class Category(models.Model):
    name = models.TextField()
    filename = models.TextField(blank=True, null=True)
