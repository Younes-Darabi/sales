from django.shortcuts import render
from django.views.generic.list import ListView
from sales.models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = "sales/list.html"
