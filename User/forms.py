from django import forms
from .models import CustomerAccount
from .constraint import GENDER_TYPE
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'gender','password1', 'password2']
    
    def save(self, commit = True):
        customer = super().save(commit=False)
        if commit == True:
            customer.save()
            gender = self.cleaned_data.get('gender')

            CustomerAccount.objects.create(
                customer = customer,
                gender = gender,
                customer_iid = 100+customer.id
            )
        return customer
    