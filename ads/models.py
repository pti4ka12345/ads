from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=1000)


class Ad(models.Model):
	name = models.CharField(max_length=1000)
	author = models.CharField(max_length=1000)
	price = models.PositiveIntegerField()
	description = models.CharField(max_length=1000, null=True)
	is_published = models.BooleanField(default=False)
