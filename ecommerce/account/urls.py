from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('register/', views.account_register, name='account_register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('login/', views.user_login, name='user_login'),

    
]