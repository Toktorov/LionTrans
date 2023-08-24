from django.shortcuts import render

from apps.settings.models import Setting
from apps.cars.models import CarInStock

# Create your views here.
def car_in_stock(request):
    setting = Setting.objects.latest('id')
    cars = CarInStock.objects.all()
    return render(request, 'car_in_stock.html', locals())

def car_in_stock_detail(request, id):
    setting = Setting.objects.latest('id')
    car = CarInStock.objects.get(id = id)
    return render(request, 'car_in_stock_detail.html', locals())