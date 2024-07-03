from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from .forms import CustomerRegistrationForm
from django.contrib.auth import login, logout,update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from books.models import Book
from django.views.generic import CreateView, ListView
from django.db.models import Sum
from datetime import datetime
# Create your views here.

class CustomerRegistrationView(FormView):
    template_name ='registration.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        customer = form.save()
        messages.success(self.request, 'Account Created Successfully')
        login(self.request, customer)
        return super().form_valid(form)

class CustomerLoginView(LoginView):
    template_name ='registration.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, "Logged in SuccessFul")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"Logged in Information is incorrect")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@login_required
def customer_logout(request):
    logout(request)
    return redirect('registraion')

@login_required
def profile(request):
    data = Book.objects.all()
    return render(request, 'profile.html', {'data' : data})

    

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('transaction_report')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form})







    
