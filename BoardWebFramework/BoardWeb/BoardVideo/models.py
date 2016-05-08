from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MainViewHelper(models.Model):
    imageField = models.FileField(upload_to="static", blank=True)
