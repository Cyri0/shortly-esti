from django.db import models

# Create your models here.
class ShortLink(models.Model):
    originalURL = models.URLField()
    active = models.BooleanField(default=True)