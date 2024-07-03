from django.urls import path
from .views import CustomerRegistrationView, CustomerLoginView,profile,customer_logout,pass_change
urlpatterns = [
    path('registraion/', CustomerRegistrationView.as_view(), name='registraion'),
    path('login/', CustomerLoginView.as_view(), name='login'),
    path('logout/', customer_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('pass_change/',pass_change,name='pass_change'),
]
