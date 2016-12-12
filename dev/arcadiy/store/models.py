"""
1) Change your models (in models.py).
2) Run python manage.py makemigrations to create migrations for those changes
3_ Run python manage.py migrate to apply those changes to the database.
"""
import os
import datetime

from django.db import models
from django.utils import timezone


#ADMIN = os.()

class Product(models.Model):
	name = models.CharField(max_length=40)
	description = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published')
	is_sold = models.BooleanField(default=False)
	price = models.CharField(max_length=1000)
	product_seller = models.CharField(default='ADMIN', max_length=20)


	def __str__(self):
		return self.id + ' ' + self.pub_date

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timdelta(days=1)

	def sold_product(self):
		self.is_sold = True

	#def post_product(self):
	#def delete(self):
	