from django.db import models
from account.models import UserBase
import secrets
from .paystack import Paystack

# Create your models here.


class Order(models.Model):
    PENDING = 'Pending'
    DELIVERED = 'Delivered'
    STATUS = [
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
    ]
    user = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    post_code = models.CharField(max_length=15, blank=True, verbose_name='Postal/ZIP code')
    country = models.CharField(max_length=100, verbose_name='Country')
    state = models.CharField(max_length=100, verbose_name='State')
    address = models.CharField(max_length=100, verbose_name='Shipping Address')
    status = models.CharField(max_length=10, choices=STATUS, default=PENDING)
    request = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'OR{self.created.strftime('%d%m%y')}{self.pk}'
    
    class Meta:
	    ordering = ('-created',)
    
class Payment(models.Model):
    user = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment: {self.amount}"
    
    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref = ref)
            if not object_with_similar_ref:
                self.ref = ref
    
        super().save(*args, **kwargs)

    def amount_value(self):
        return int(self.amount) * 100
    
    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

    class Meta:
	    ordering = ('-date_created',)
         


    