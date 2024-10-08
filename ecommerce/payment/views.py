from django.shortcuts import render
from .models import Payment
from cart.cart import Cart

# Create your views here.
def verify_payment(request, ref):
	payment = Payment.objects.get(ref=ref)
	payment.verify_payment()
	cart = Cart(request)

	return render(request, "frontend/success.html", {'cart':cart})