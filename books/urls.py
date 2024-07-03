from django.urls import path
from .views import add_balance,DetailsPostView,Brrow_Book,Return_Book,CommentPostView
urlpatterns = [
    path('add_balance/', add_balance, name='add_balance'),
    path('details/<int:id>/', DetailsPostView.as_view(), name='details_post'),
    path('Brrow_Book/<int:id>/', Brrow_Book, name='Brrow_Book'),
    path('return_Book/<int:id>/',Return_Book, name='return_Book'),
    path('comment_post/<int:id>',CommentPostView.as_view(), name='comment_post'),
]
