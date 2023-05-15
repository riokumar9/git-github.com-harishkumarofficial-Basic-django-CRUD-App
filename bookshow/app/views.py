from django.shortcuts import render\

# import class_based view
from rest_framework.decorators import APIView,permission_classes

# import request and response
from rest_framework.response import Response

# import status code
from rest_framework import status

# import models
from .models import BookCategory,BookDeatils

# import serializers
from .serializers import BookCategorySerializer,BookDeatilsSerializer

# import IsAuthenticated
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse

from rest_framework.pagination import PageNumberPagination
from .pagination import LargeResultsSetPagination
from rest_framework.parsers import MultiPartParser, FormParser

# This Class is a BookCategory View
class BookCategoryView(APIView):
    # pagination_class = PageNumberPagination
    serializer_class = BookCategorySerializer

    # Get The All The Book Category View
    def get(self,request):
        paginator = PageNumberPagination()
        queryset = BookCategory.objects.all()
        # context = queryset(queryset,request)
        serializer  = self.serializer_class(queryset,many = True)
        return paginator.get_paginated_response(serializer.data)

    # Post the Book Category 
    def post(self,request):
         serializer = self.serializer_class(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    # Create a Book Category
    def put(self, request, slug):
        try:
            queryset = BookCategory.objects.get(slug=slug)
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BookDeatils.DoesNotExist:
            return Response({'message': 'Book Category does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Deleted a book category
    def delete(self, request, slug):
        try:
            Bookes = BookCategory.objects.filter(slug=slug)
            Bookes.delete() 
            return Response({'message': 'Book category deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except BookDeatils.DoesNotExist:
            return Response({'message': 'Book Category does not exist'}, status=status.HTTP_404_NOT_FOUND)

class SingleBookCategoryView(APIView):
    serializer_class = BookCategorySerializer

  # This is a single book category 
    def get(self,request,slug):

        try:
            context = BookCategory.objects.get(slug=slug)
            serializer = self.serializer_class(context)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except BookCategory.DoesNotExist:
            return Response({'message' : 'Record Not Found'},status = status.HTTP_404_NOT_FOUND)

# This class is a BookDetails view
class BookDetailsView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    pagination_class = LargeResultsSetPagination
    serializer_class = BookDeatilsSerializer
    
    # Get the All the Book Details
    def get(self,request):
        paginator = PageNumberPagination() 
        queryset = BookDeatils.objects.all()
        context = paginator.paginate_queryset(queryset,request)
        serializer = self.serializer_class(context,many =True)
        # return paginator.get_paginated_response(serializer.data)
        return render(request, "index.html", context)    

    # Create a Book
    def post(self,request,slug):
        queryset = BookCategory.objects.get(slug=slug)
        serializer = self.serializer_class(queryset,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    # updated a Book
    def put(self, request, slug):
        try:
            queryset = BookDeatils.objects.get(slug=slug)
            serializer = self.serializer_class(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BookDeatils.DoesNotExist:
            return Response({'message': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Deleted a book
    def delete(self, request, slug):
        try:
            Bookes = BookDeatils.objects.get(slug=slug)
            Bookes.delete()
            return Response({'message': 'Book category deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except BookDeatils.DoesNotExist:
            return Response({'message': 'Book category does not exist'}, status=status.HTTP_404_NOT_FOUND)
