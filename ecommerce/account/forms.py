from django import forms
from .models import UserBase

class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(
        label='Fullname', min_length=4, max_length=50, help_text='Required'
    ) 
    email = forms.EmailField(
       max_length=100, help_text='Required', error_messages={'required':'You will need an email address'} 
    )
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput
    )

    class Meta:
        model = UserBase
        fields = ('email', 'user_name')

    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password does not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Email already taken! Please use another Email. '
            )    
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Full name', }
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Email', 'name':'email' }
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Enter Password', }
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Confirm Password', }
        )
        