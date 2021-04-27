from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
	date = models.CharField('date', max_length=100)
	balance = models.IntegerField(verbose_name='balance', null=True)

	USERNAME_FIELD = "username"
	REQUIRED_FIELD = []

	def __str__(self):
		return f'{self.first_name} {self.last_name} {self.username}'

