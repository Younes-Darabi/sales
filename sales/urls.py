from django.urls import path
from sales.views import CustomerListView

urlpatterns = [
    path('', CustomerListView.as_view()),
]
