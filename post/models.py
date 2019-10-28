from django.db import models
from tinymce import models as tinymce_models


class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    content = tinymce_models.HTMLField()
