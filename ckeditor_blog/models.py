from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    content = RichTextField()

