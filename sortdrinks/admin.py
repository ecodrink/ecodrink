from django.contrib import admin

from .models import Drink, Category, Style


class SortDrinksAdmin(admin.ModelAdmin):
    readonly_fields = ('score',)


admin.site.register(Drink, SortDrinksAdmin)
admin.site.register(Category)
admin.site.register(Style)
