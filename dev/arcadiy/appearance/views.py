from django.shortcuts import render
from django.http import	HttpResponse

def index(request):
	index_page = open('/appearance/templates/index.html')
	return HttpResponse(index_page)
	index_page.close()