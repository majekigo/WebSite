from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def api(request):
    return render(request, template_name='api/api.html')


def create(request, product_id):
    return HttpResponse(f"Добавление {product_id}")


def delete(request, product_id):
    return HttpResponse(f"Удаление {product_id}")


def read(request, product_id):
    return HttpResponse(f"Чтение {product_id}")


def update(request, product_id):
    return HttpResponse(f"Изменение {product_id}")