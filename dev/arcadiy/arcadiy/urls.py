from django.conf.urls import include, url
from appearance.views import MainView, ContactView

urlpatterns = [
    url(r'^' , MainView.as_view()),
    url(r'^contact/', ContactView.as_view()),
]
