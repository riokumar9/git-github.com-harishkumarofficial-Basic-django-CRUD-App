from rest_framework import serializers

#import models
from .models import BookCategory,BookDeatils


# Book_Category Serializer
class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields =  ["category_name","slug"]

# Book_Deatils Serializer
class BookDeatilsSerializer(serializers.ModelSerializer):
     category = BookCategorySerializer(read_only = True)  
     class Meta:
        model = BookDeatils
        fields = ["title","author_name","category","slug","thumbnail_image"]


        