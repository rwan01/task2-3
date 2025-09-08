

# from django.shortcuts import render, get_object_or_404
# from .models import Product

# def products(request):
#     query = request.GET.get("q")
#     items = Product.objects.all()

#     if query:
#         items = items.filter(name__icontains=query)  # only search by name
#     return render(request, 'products/products.html', {'items': items, 'query': query})


# def product(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'products/product.html', {'product': product})


from django.shortcuts import render, get_object_or_404
from .models import Product

def products(request):
    query = request.GET.get("q")        # search by name
    category = request.GET.get("category")  # filter by genre
    items = Product.objects.all()

    if query:
        items = items.filter(name__icontains=query)

    if category and category != "All":
        items = items.filter(genre=category)

    # Pass selected category to template to keep it selected
    context = {
        'items': items,
        'query': query,
        'selected_category': category or "All",
        'categories': ["All", "Paint", "Status"]
    }
    return render(request, 'products/products.html', context)

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product.html', {'product': product})
