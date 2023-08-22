from django.contrib import admin

from apps.cars.models import CarInStock

# Register your models here.
@admin.register(CarInStock)
class CarInStockAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year')