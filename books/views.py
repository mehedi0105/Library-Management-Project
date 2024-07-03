from django.shortcuts import render,redirect
from . import forms
from User.models import CustomerAccount
from django.contrib import messages
from django.core.mail import EmailMessage ,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from . import models
from django.utils import timezone
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

@login_required
def add_balance(request):
    if request.method == 'POST':
        form = forms.AddBalanceForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['amount'])
            amount = form.cleaned_data['amount']
            # account =request.user.account.balance
            # print(request.user.balance)
            account, created = CustomerAccount.objects.get_or_create(customer=request.user)
            print(account.balance)
            account.balance+=amount
            messages.success(request, "Add Money in SuccessFul")
            account.save(
            update_fields=[
                'balance'
            ]
        )
            print(account.balance)
            mail_subject = "Add Balance Message"
            message = render_to_string('add_balance_email.html',{
             'user' : request.user,
             'amount':amount,
             }                            
            )
            to_email = request.user.email
            send_email = EmailMultiAlternatives(mail_subject, '', to=[to_email])
            send_email.attach_alternative(message, 'text/html')
            send_email.send()
            return redirect('add_balance')
    else:
        form = forms.AddBalanceForm()
    return render(request, 'add_balance.html',{'form':form})


class DetailsPostView(DetailView):
    model = models.Book
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'


def Brrow_Book(request, id):
    book = models.Book.objects.get(pk=id)
    if request.user.customer.balance >= book.borrow_price:
        request.user.customer.balance -= book.borrow_price
        book.borrow_date = timezone.now()
        book.borrow = True
        book.save(update_fields=['borrow_date','borrow'])
        print(book.borrow)

        request.user.customer.save(update_fields=['balance'])
        print(book.borrow_price)

        mail_subject = "Book Borrow Message"
        message = render_to_string('borrow.html',
                {
                'user' : request.user,
                'amount':book.borrow_price,
                'title':book.title,
                }                            
            )
        messages.success(request, f'Borrow Book {book.title} successful.')
        to_email = request.user.email
        send_email = EmailMultiAlternatives(mail_subject, '', to=[to_email])
        send_email.attach_alternative(message, 'text/html')
        send_email.send()
        return redirect('profile')
    else:
       messages.error(request,f'Insufficient  Balance')
       return redirect('homepage')
    

def Return_Book(request, id):
    book = models.Book.objects.get(pk=id)
    request.user.customer.balance += book.borrow_price
    book.return_date =timezone.now()
    book.borrow = False
    book.save(update_fields=['return_date','borrow'])
    print(book.borrow)

    request.user.customer.save(update_fields=['balance'])
    print(book.borrow_price)
    messages.success(request, f'Return Book {book.title} successful.')
    mail_subject = "Book Return Message"
    message = render_to_string('borrow.html',
                {
                'user' : request.user,
                'amount':book.borrow_price,
                'title':book.title,
                }                            
            )
    to_email = request.user.email
    send_email = EmailMultiAlternatives(mail_subject, '', to=[to_email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()
    return redirect('homepage')

class CommentPostView(DetailView):
    model = models.Book
    pk_url_kwarg = 'id'
    template_name = 'comment.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
