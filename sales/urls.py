from django.contrib import admin
from django.urls import path
from sales.views import Home_Page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home_Page),
]
