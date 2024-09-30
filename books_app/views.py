from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction
# from django.views import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# class BookksListView(ListView):
#     paginate_by = 2
#     model = Book

class BooksApi(APIView):
    def get(self, request, id=None):
        if id:
            if Book.objects.filter(id= id).exists():
                books = Book.objects.get(id= id)
                serializerd_data = BookSerializer(books)
                return Response({
                    'success': True,
                    'data':serializerd_data.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'success': False,
                    'data':'Book not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
        # import pdb;pdb.set_trace()
        if request.GET.get('title') and request.GET.get('author'):
            books = Book.objects.filter(title=request.GET.get('title'), author=request.GET.get('author'))
        elif request.GET.get('title'):
            books = Book.objects.filter(title=request.GET.get('title'))
        elif request.GET.get('author'):
            books = Book.objects.filter(author=request.GET.get('author'))
        else:
            books = Book.objects.all()
        if request.GET.get('page'):
            page_count= request.GET.get('count', 2) or 2
            pages = Paginator(books, page_count)
            page_no = request.GET.get('page', 1) or 1
            if int(page_no) > pages.num_pages:
                return Response({
                    'success': False,
                    'data':"Empty page"
                }, status=status.HTTP_404_NOT_FOUND)
            data = pages.get_page(page_no)
            books = data.object_list
        serializerd_data = BookSerializer(books, many=True)
        return Response({
            'success': True,
            'data':serializerd_data.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request):
        # import pdb;pdb.set_trace()
        with transaction.atomic():
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                    'data':serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                'success': False,
                'data':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id= None):
        with transaction.atomic():
            book = Book.objects.get(id= id)
            serializer = BookSerializer(book, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'success': True,
                }, status=status.HTTP_200_OK)
            return Response({
                'success': False,
                'data':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id= None):
        book = Book.objects.filter(id=id).delete()
        return Response({
            'success': False,
            'data':"Successfully deleted"
        }, status=status.HTTP_200_OK)