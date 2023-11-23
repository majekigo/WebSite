from django.shortcuts import render
# Create your views here.


def catalog(request):
    return render(request, template_name='catalogs/catalog.html')


def catalog2(request):
    return render(request, template_name='catalogs/catalog2.html')


def product_withdrawal(request):
    return render(request, template_name='catalogs/product_withdrawal.html')


def feedback(request):
    return render(request, template_name='catalogs/feedback.html')


def index(reques):
    return render(reques, template_name='catalogs/index.html')