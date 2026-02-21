from django.urls import path
from sales.views import CustomerListSearchView, CustomerListView, CustomerDetailView

urlpatterns = [
    path('', CustomerListView.as_view()),
    path('<str:name>/', CustomerListSearchView.as_view()),
    path('customer/<int:pk>/', CustomerDetailView.as_view())
]
