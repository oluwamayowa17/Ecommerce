from django.urls import path
from shopapp import views



app_name = 'shopapp'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('products/', views.products, name='products'),
    path('product/details/<slug:slug>', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),

]