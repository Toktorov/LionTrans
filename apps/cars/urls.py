from django.urls import path 

from apps.cars.views import car_in_stock_detail, car_in_stock


urlpatterns = [
    path('', car_in_stock, name='car_in_stock'),
    path('<int:id>/', car_in_stock_detail, name='car_in_stock_detail')
]