from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_filter = ["first_name", "last_name"]
    # list_display = ["last_name", "account"]
    # fields=["last_name", "account"]

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
                "fields": ["newsletter_abo","slug"],
            },
        ),
    ]


admin.site.register(Customer, CustomerAdmin)
