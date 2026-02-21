from django.shortcuts import render
from django.views.generic.list import ListView
from sales.models import Customer
from django.views.generic.detail import DetailView


class CustomerListView(ListView):
    model = Customer
    # queryset = Customer.objects.filter(first_name__icontains="Jo")
    template_name = "sales/list.html"
    paginate_by = 3


class CustomerListSearchView(CustomerListView):
    def get_queryset(self):
        name = self.kwargs.get("name")
        return Customer.objects.filter(first_name__icontains=name)

from django.utils import timezone
class CustomerDetailView(DetailView):
    model = Customer
    template_name = "sales/detail.html"

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        return obj