from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['user', 'created', 'updated', 'status']
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Phone Number',
            }),
            'post_code': forms.TextInput(attrs={
                'placeholder': 'Post Code',
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Select Country',
            }),
            'state': forms.TextInput(attrs={
                'placeholder': 'City',
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Shipping Address',
            }),
            'request': forms.Textarea(attrs={
                'placeholder': 'Special Request...',
            }),
        }