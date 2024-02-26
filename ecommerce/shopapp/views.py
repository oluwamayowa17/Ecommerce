from django.shortcuts import render, get_object_or_404
from shopapp.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Create your views here.

def index(request):
    products = Products.objects.all().order_by('-created')[:3]
    deal = HotDeal.objects.all()
    for product in products:
            hot_deal = HotDeal.objects.filter(product=product).first()
            if hot_deal:
                discount_price = hot_deal.discount / 100 * product.price
                product.discount_price = product.price - discount_price
            else:
                product.discount_price = None   
    news = News.objects.all()
    context = {
        'product': products,
        'deal':deal,
        'news':news
    }
    return render(request, 'frontend/index.html', context)



def about(request):
    context = {}
    return render(request, 'frontend/about.html', context)

def products(request):
    product = Products.objects.all().order_by('-created')
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
    categories = prod.category.all()

    related_products = []

    for category in categories:
        category_products = category.products.exclude(slug=slug)  # Exclude the current product
        related_products.extend(category_products)

    context={
        'prod': prod,
        'related_products':related_products,
    }
    return render (request, 'frontend/single-product.html', context)

def hot_deal_details(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    hot_deal = get_object_or_404(HotDeal, product=product)

    discount_price = None
    if hot_deal:
        discount_price = int(abs(hot_deal.discount / 100 * product.price - product.price))
    context={
        'hot_deal':hot_deal,
        'discount_price':discount_price,
    }
    return render(request, 'frontend/hotdeal.html', context)

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

def news_details(request):
    context = {}
    return render(request, 'frontend/single-news.html', context )

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact(name=name, email=email, phone=phone, subject=subject,  message=message)
        mail_subject = subject
        email_data = {
                'name':name,
                'email':email,
                'phone':phone,
                'subject':subject,
                'message':message
        }
        html_message = render_to_string('frontend/mail-template.html', email_data)
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send = mail.send_mail(mail_subject, plain_message, from_email, ['ogungburemayowa2019@gmail.com'], html_message=html_message)
        if send:
            data.save()
            mail.send_mail(subject, plain_message, from_email, [ 'ogungburemayowa2019@gmail.com'], html_message=html_message)
            print(name, email, phone, message)
    context = {}
    return render(request, 'frontend/contact.html', context)