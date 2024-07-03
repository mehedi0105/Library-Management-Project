from django import forms
from .models import AddBalance, Book, Comment

class AddBalanceForm(forms.ModelForm):
    class Meta:
        model = AddBalance
        fields = ['amount']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['writer']

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name','email','body']
        # exclude = ['author']