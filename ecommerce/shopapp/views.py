from django.shortcuts import render, get_object_or_404
from shopapp.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    product = Products.objects.all().order_by('created')
    news = News.objects.all()
    context = {
        'product': product,
        'news':news
    }
    return render(request, 'frontend/index.html', context)

def about(request):
    context = {}
    return render(request, 'frontend/about.html', context)

def products(request):
    product = Products.objects.all()
    category = Category.objects.all()
    page = request.GET.get('page')
    num_of_items = 3
    paginator = Paginator(product, num_of_items) 
    try:
        product = paginator.page(page) 
    except PageNotAnInteger:
        page = 1
        product = paginator.page(page)  
    except EmptyPage:
        page = paginator.num_pages
        product = paginator.page(page)
    context = {
        'product': product,
        'paginator': paginator,
        'category': category,
    }
    return render(request, 'frontend/shop.html', context)

def product_detail(request, slug):
    prod = get_object_or_404(Products, slug=slug)
    context={
        'prod': prod,
    }
    return render (request, 'frontend/single-product.html', context)

def cart(request):
    context = {}
    return render(request, 'frontend/cart.html', context)

def news(request):
    news = News.objects.all()
    page = request.GET.get('page')
    num_of_items = 3
    paginator = Paginator(news, num_of_items)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        news = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        product = paginator.page(page)
    context = {
        'news': news,
        'paginator': paginator,
    }
    return render(request, 'frontend/news.html', context)

def contact(request):
    context = {}
    return render(request, 'frontend/contact.html', context)