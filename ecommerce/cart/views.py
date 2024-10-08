from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from shopapp.models import Products
from django.http import JsonResponse
from payment.forms import CheckoutForm
from django.conf import settings
from payment.models import Payment

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'frontend/cart.html', {'cart': cart})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Products, id=product_id)
        cart.add(product=product, qty = product_qty)

        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)
        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        final_total = cart.final_price()

        response = JsonResponse({
            'qty': cartqty,
            'subtotal': carttotal,
            'final_total': final_total,
        })
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_id, qty=product_qty)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        final_total = cart.final_price()
        
        updated_item = cart.cart[str(product_id)]
        updated_total_price = float(updated_item['price']) * updated_item['qty']

        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal, 'total_price': updated_total_price, 'final_total': final_total})
        return response

def checkout(request):
    cart = Cart(request)
    payment = None  
    ref = None
    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            payment = Payment.objects.create(user=request.user, amount=cart.final_price())
            ref = payment.ref 
            checkout_instance = checkout_form.save(commit=False)
            checkout_instance.user = request.user
            checkout_instance.save()

            return render(request, 'frontend/checkout.html', {
                'cart': cart,
                'checkout_form': checkout_form,
                'payment': payment,
                'ref': ref,  
                'field_values': request.POST,
                'paystack_pub_key': settings.PAYSTACK_PUBLIC_KEY,
            })
    else:
        checkout_form = CheckoutForm()
    
    context = {
        'cart': cart,
        'checkout_form': checkout_form,
    }
    
    return render(request, 'frontend/checkout.html', context)
