from django.db import models
from User.models import CustomerAccount
from category.models import Category
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class AddBalance(models.Model):
    account = models.ForeignKey(CustomerAccount, related_name='AddBalance', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    after_balance = models.DecimalField(decimal_places=2, max_digits=12)

class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/media/uploads', blank=True, null=True)
    borrow_price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    borrow_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    borrow = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comments by {self}"