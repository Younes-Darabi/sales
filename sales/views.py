from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from sales.models import Customer

class Customer_View(View):

    def get(self, request):
        ChatDB = list(Customer.objects.values())
        return JsonResponse(ChatDB, safe=False)
