from django.urls import path
from .views import BooksApi

urlpatterns = [
    path('', BooksApi.as_view(), name='books'),
    path('<int:id>/', BooksApi.as_view(), name='books'),
]