from django.contrib import admin
from .models import Bill, Customer, Order, Product, Producttype


class CustomerAdmin(admin.ModelAdmin):
    list_filter = ["first_name", "last_name"]
    list_display = ["first_name", "account"]
    readonly_fields = ["account"]
    prepopulated_fields = {"slug":["first_name", "last_name"]}
    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name", "account"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["newsletter_abo"],
            },
        ),
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]

class BillAdmin(admin.ModelAdmin):
    list_display = ["total_amount","is_paid"]

class ProducttypeAdmin(admin.ModelAdmin):
    list_display = ["order","product", "type_name"]
    

class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "bill"]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Producttype, ProducttypeAdmin)
admin.site.register(Order, OrderAdmin)
