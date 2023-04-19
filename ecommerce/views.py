from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


def product_page(request):
    products = Product.objects.all()
    c = {
        "products": products
    }
    return render(request, "ecommerce/products.html", c)


def about_page(request):
    return HttpResponse("About Page")




