from django.contrib import admin

from apps.cars.models import CarInStock, CarInStockImage

# Register your models here.
class PostImageAdminTabularInline(admin.TabularInline):
    model = CarInStockImage
    extra = 1

@admin.register(CarInStock)
class CarInStockAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year')
    inlines = [PostImageAdminTabularInline]

@admin.register(CarInStockImage)
class CarInStockImageAdmin(admin.ModelAdmin):
    list_display = ('car', 'image')

