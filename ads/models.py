from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    is_published = models.BooleanField(default=False, blank=True)
