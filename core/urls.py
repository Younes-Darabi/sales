from django.contrib import admin
from django.urls import include, path
from sales import urls

urlpatterns = [
    path('',include(urls) ),
]
