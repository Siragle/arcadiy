"""
1) Change your models (in models.py).
2) Run python manage.py makemigrations to create migrations for those changes
3_ Run python manage.py migrate to apply those changes to the database.
"""

import datetime

from django.db import models
from django.utils import timezone


class Users(models.Model):
	login = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.login + ' ' + self.password + ' ' + str(self.pub_date)

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timdelta(days=1)
#class Admin(models.Model):

