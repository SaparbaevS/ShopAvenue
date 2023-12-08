from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, ListView, CreateView, UpdateView, DeleteView

from products.forms import ProductModelForm
from products.models import Category, Product


class StartPageView(TemplateView):
    template_name = 'shop/product/start.html'


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'shop/product/product_detail.html'
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'


class ProductAddView(CreateView):
    model = Product
    form_class = modelform_factory(Product, fields=['category', 'name', 'image', 'description', 'price'])
    template_name = 'shop/product/add_product.html'
    success_url = reverse_lazy('products:list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'shop/product/update.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'
    success_url = reverse_lazy('products:list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/product/delete.html'
    slug_url_kwarg = 'slug_param'
    success_url = reverse_lazy('products:list')




# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'shop/product/product_list.html',
#                   {
#                       'category': category,
#                       'categories': categories,
#                       'products': products
#                   })

# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     return render(request, 'shop/product/product_detail.html', {'product': product})
