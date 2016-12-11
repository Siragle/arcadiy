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
	# def __init__(self, id, name, description, img, pub_date, product_seller, price=0, is_sold=False):
	name = models.CharField(max_length=40)
	description = models.CharField(max_length=150)
	pub_date = models.DateTimeField('date published')
	# is_sold = False
#	product_seller = ADMIN

	def __str__(self):
		return self.id + ' ' + self.pub_date

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timdelta(days=1)

	def sold_product(self):
		self.is_sold = True

	#def post_product(self):
	#def delete(self):