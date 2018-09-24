from django.contrib import admin

from .models import Drink, Category, Style


admin.site.register(Drink)
admin.site.register(Category)
admin.site.register(Style)
