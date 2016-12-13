from django.shortcuts import render
from django.http import	HttpResponse
from users.models import User

class UserList(ListView):
	model = User
	context_object_name = 'users'