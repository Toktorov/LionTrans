from django.shortcuts import render
from django.core.paginator import Paginator
import requests

from apps.settings.models import Setting
from apps.cars.models import CarInStock

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    cars = CarInStock.objects.all()

    api_url = 'https://auctionauto.kg/api/v1/vehicle/?find=%7B%22saleDate%22:%7B%22$ne%22:null,%22$gt%22:1692681953548%7D%7D&limit=20&page=1&sort=%7B%22sortOrder%22:-1,%22updatedAt%22:-1%7D'
    
    # Получение значения параметра page из GET-запроса
    page_number = request.GET.get('page', 1)

    # Отправьте запрос к API с параметром page
    response = requests.get(api_url, params={'page': page_number})

    # Проверьте статус ответа
    if response.status_code == 200:
        # Разберите JSON-ответ
        data = response.json()
        vehicles = data.get('items', [])

        # Создание объекта Paginator для пагинации
        paginator = Paginator(vehicles, per_page=20)  # Здесь 10 - количество элементов на странице

        # Получение запрошенной страницы
        page = paginator.get_page(page_number)

        # Передайте данные в шаблон для отображения
        return render(request, 'index3.html', locals())
    else:
        # Если запрос к API завершился неудачей, обработайте ошибку
        error_message = 'Не удалось получить данные с API.'
        return render(request, 'index3.html', locals())

def auction(request):
    setting = Setting.objects.latest('id')

    api_url = 'https://auctionauto.kg/api/v1/vehicle/?find=%7B%22saleDate%22:%7B%22$ne%22:null,%22$gt%22:1692619163562%7D%7D&limit=20&page=1&sort=%7B%22sortOrder%22:-1,%22updatedAt%22:-1%7D'

    # Получение значения параметра page из GET-запроса
    page_number = request.GET.get('page', 1)

    # Отправьте запрос к API с параметром page
    response = requests.get(api_url, params={'page': page_number})

    # Проверьте статус ответа
    if response.status_code == 200:
        # Разберите JSON-ответ
        data = response.json()
        vehicles = data.get('items', [])

        # Создание объекта Paginator для пагинации
        paginator = Paginator(vehicles, per_page=20)  # Здесь 10 - количество элементов на странице

        # Получение запрошенной страницы
        page = paginator.get_page(page_number)

        # Передайте данные в шаблон для отображения
        return render(request, 'auction.html', locals())
    else:
        # Если запрос к API завершился неудачей, обработайте ошибку
        error_message = 'Не удалось получить данные с API.'
        return render(request, 'auction.html', locals())

def auction_detail(request, id):
    setting = Setting.objects.latest('id')

    api_url = f'https://auctionauto.kg/api/v1/vehicle/{id}'
    # Отправьте запрос к API
    response = requests.get(api_url)

    # Проверьте статус ответа
    if response.status_code == 200:
        # Разберите JSON-ответ
        vehicle = response.json()
        # vehicle = data.get('items', [])
        # print(vehicle)

        # Передайте данные в шаблон для отображения
        return render(request, 'auction_detail.html', locals())


def search(request):
    setting = Setting.objects.latest('id')
    # Получите параметр поиска из GET-запроса
    search_query = request.POST.get('q')
    print("Search:", search_query)
    # Формируйте URL для выполнения поискового запроса
    api_url = f'https://auctionauto.kg/api/v1/vehicle/search/?query={search_query}'

    # Отправьте запрос к API
    response = requests.post(api_url)

    # Проверьте статус ответа
    if response.status_code == 200:
        # Разберите JSON-ответ
        data = response.json()
        vehicles = data.get('items', [])

        # Передайте данные в шаблон для отображения
        return render(request, 'search_results.html', locals())
    else:
        # Если запрос к API завершился неудачей, обработайте ошибку
        error_message = 'Не удалось выполнить поиск.'
        return render(request, 'search_results.html', locals())

def contact(request):
    setting = Setting.objects.latest('id')
    return render(request, 'contact.html', locals())

def check_vehicle(request):
    api_url = 'https://auctionauto.kg/api/v1/vehicle'

    # Отправьте запрос к API
    response = requests.get(api_url)

    # Проверьте статус ответа
    if response.status_code == 200:
        # Разберите JSON-ответ
        data = response.json()
        vehicles = data.get('items', [])

        print(vehicles)
        # Передайте данные в шаблон для отображения
        return render(request, 'check.html', {'vehicles': vehicles})