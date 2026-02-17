from django.contrib import admin
from django.urls import path
from sales import views

urlpatterns = [
    path('', views.Customer_View.as_view()),
]
