from django.conf.urls import url
from .views import api

urlpatterns = [
    url(r'^first', api)
]
