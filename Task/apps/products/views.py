from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from .models import Product

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def product_table(request):
    products = Product.objects.all().order_by('-changed_date')
    return render(request, 'products/product_table.html', {'products': products})


def product_as_json(request):
    products = Product.objects.all().order_by('-changed_date')
    json = serializers.serialize('json', products)
    return HttpResponse(json, content_type='application/json')
