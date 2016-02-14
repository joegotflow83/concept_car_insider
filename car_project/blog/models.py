from django.db import models
from uuslug import uuslug


class Post(models.Model):
	"""Allow users to create posts to the blog"""

	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	content = models.TextField()
	image = models.ImageField(upload_to="img", blank=True, null=True)
	tag = models.CharField(max_length=32)
	views = models.IntegerField(default=0)
	slug = models.CharField(max_length=128, unique=True)

	def __str__(self):
		"""Prettify output of title"""
		return self.title

	def save(self, *args, **kwargs):
		"""Save slug for unique post urls"""
		super(Post, self).save(*args, **kwargs)