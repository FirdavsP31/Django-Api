from django.shortcuts import render,get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView)
# Create your views here.

from .serializer import  *
from books.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# class BooksApiView(ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializerClass

# class BookDetailView(RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializerClass

# class BookCreateAPiView(CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializerClass

# class BookUpdateView(UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializerClass

# class BookDestroyAPiView(DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializerClass

class BooksApiView(APIView):
    def get(request,self):
        books = Books.objects.all()
        serializer_data = BooksSerializerClass(books,many=True).data
        data = {
            'status': 'Kitaplar qaytarildi',
            'books' : serializer_data
        }
        return Response(data)
    
class BookDetailView(APIView):
    def get(self,request,pk):
        book = Books.objects.get(id=pk)
        serializer_data = BooksSerializerClass(book).data
        data = {
            'status': 'Detail ashildi',
            'book': serializer_data
        }
        return Response(data)



class BookUpdateView(APIView):
    def put(self,request,pk):
        books = Books.objects.all()
        book = get_object_or_404(books,id=pk)
        data = request.data
        serializer_data = BooksSerializerClass(instance=book, data=request.data, partial=True)
        if serializer_data.is_valid():
            book_saved = serializer_data.save()
            data = {
                'status': True,
                'message' : f'Kitap ozgerildi: {book_saved}'
            }
        return Response(data)
    

class BookDestroyAPiView(APIView):
    def delete(self,request,pk):
        books = Books.objects.all()
        book = get_object_or_404(books,id=pk)
        book.delete()
        data = {
            'status': True,
            'message': 'oshirildi'
        }
        return Response(data,status=status.HTTP_200_OK)
    


# class BookCreateAPiView(APIView):
#     def post(self,request):
#         data = request.data
#         serializer = BooksSerializerClass(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': 'You added a book',
#                 'book': data
#             }
#             return Response(data,status=status.HTTP_201_CREATED)

class BookCreateAPiView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializerClass    