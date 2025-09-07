# from django.shortcuts import render
from django.shortcuts import render ,get_object_or_404# type: ignore
from .models import Product

# Create your views here.

# def products(request):
#     return render(request, 'products/products.html',{'Product' : Product.objects.all()})


# def products(request):
#     items = Product.objects.all()
#     return render(request, 'products/products.html', {'items': items})

# def product(request):
#     return render(request, 'products/product.html')


def products(request):
    items = Product.objects.all()
    return render(request, 'products/products.html', {'items': items})

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product.html', {'product': product})
