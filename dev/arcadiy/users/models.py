"""
1) Change your models (in models.py).
2) Run python manage.py makemigrations to create migrations for those changes
3_ Run python manage.py migrate to apply those changes to the database.
"""
import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
	login = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	registered_date = models.DateTimeField('date registered')

	def __str__(self):
		return self.login + ' ' + self.password + ' ' + str(self.registered_date)

	def was_published_recently(self):
		return self.registered_date >= timezone.now() - datetime.timdelta(days=1)

