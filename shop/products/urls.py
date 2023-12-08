from django.urls import path

from products.views import ProductDetailView, StartPageView, ProductListView, ProductAddView, ProductUpdateView, \
    ProductDeleteView

app_name = 'products'

urlpatterns = [
    path('', StartPageView.as_view(), name='start'),
    path('products/', ProductListView.as_view(), name='list'),
    path('product/add/', ProductAddView.as_view(), name='add'),

    path('products/<slug:slug_param>/', ProductDetailView.as_view(), name='detail'),
    path('product/<slug:slug_param>/update', ProductUpdateView.as_view(), name='update'),
    path('product/<slug:slug_param>/delete', ProductDeleteView.as_view(), name='delete'),

]