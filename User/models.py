from django.db import models
from django.contrib.auth.models import User
from .constraint import GENDER_TYPE
# Create your models here.

class CustomerAccount(models.Model):
    customer = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)
    customer_iid = models.IntegerField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    add_balance_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0,max_digits=15,decimal_places=2)

    def __str__(self):
        return str(self.customer_iid)