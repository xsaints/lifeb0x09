from django.db import models
from django.urls import reverse

from django.conf import settings


class Demol(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    