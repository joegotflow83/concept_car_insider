from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	"""Allow users to customize their profile"""

	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=32, null=True)
	last_name = models.CharField(max_length=32, null=True)
	car_history = models.CharField(max_length=255)
	current_car = models.CharField(max_length=64)
	dream_car = models.CharField(max_length=64)
	favorite_brand = models.CharField(max_length=64)
	profile_pic = models.ImageField(upload_to="img", blank=True, null=True)