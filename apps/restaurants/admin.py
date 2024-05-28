from django.contrib import admin

from apps.restaurants.models import Restaurant, Hour, Restaurant_Menu
admin.site.register(Restaurant)
admin.site.register(Hour)
admin.site.register(Restaurant_Menu)