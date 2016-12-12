from django.conf.urls import include, url

urlpatterns = [
	url(r'^users/', include('users.urls')),
    url(r'^index/', include('appearance.urls')),
]
