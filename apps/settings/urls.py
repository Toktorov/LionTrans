from django.urls import path 

from apps.settings.views import index, check_vehicle, auction, auction_detail, search, contact


urlpatterns = [
    path('', index, name='index'),
    path('check/', check_vehicle, name='check_vehicle'),
    path('auction/', auction, name='auction'),
    path('auction/lot/<int:id>/', auction_detail, name='auction_detail'),
    path('search/', search, name='search'),
    path('contact/', contact, name='contact'),
]