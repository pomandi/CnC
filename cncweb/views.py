from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Collection, Product
from django.views.generic.detail import DetailView


def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    return render(request, 'cncweb/collection_detail.html', {'collection': collection})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'cncweb/product_detail.html', {'product': product})

# views.py
def home(request):
    products = Product.objects.all()[:8]  # Get the first 8 products
    for product in products:
        product.main_image = product.images.first()  # We assume the first image as the main image.
    return render(request, 'cncweb/home.html', {'products': products})


def hakkimizda(request):
    products = Product.objects.all()[:8]  # Get the first 8 products
    for product in products:
        product.main_image = product.images.first()  # We assume the first image as the main image.
    return render(request, 'cncweb/home.html', {'products': products})

def iletisim(request):
    products = Product.objects.all()[:8]  # Get the first 8 products
    for product in products:
        product.main_image = product.images.first()  # We assume the first image as the main image.
    return render(request, 'cncweb/home.html', {'products': products})

def collection_list(request):
    collections = Collection.objects.all()
    return render(request, 'cncweb/collection_list.html', {'collections': collections})

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'cncweb/collection_detail.html'
    context_object_name = 'collection'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()  # collection ile ilişkili tüm ürünleri alır
        return context
