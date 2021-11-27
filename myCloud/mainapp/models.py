from django.db import models
from django.db.models.base import Model

# Create your models here.


class File(models.Model):
    title = models.CharField(max_length=64)
    url = models.FileField()
