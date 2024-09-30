from rest_framework.serializers import Serializer, ValidationError
from .models import Book
from rest_framework import serializers

def validate_isbn(value):
    if len(value) != 13:
        raise ValidationError("ISBN must of length 13")

def validate_price(value):
    if value < 0:
        raise ValidationError("Price must be positive")

class BookSerializer(Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    published_date = serializers.DateField()
    isbn = serializers.CharField(max_length=13, validators=[validate_isbn])
    price = serializers.FloatField(validators=[validate_price])
    stock = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ['id', 'title']
    
    def update(self, instance, validated_data):
        # import pdb;pdb.set_trace()
        return Book.objects.update(**validated_data)
    
    def create(self, validated_data):
        # import pdb;pdb.set_trace()
        return Book.objects.create(**validated_data)
    
    
{
    "title": "Harry Potter",
    "author": "J K Rowling",
    "published_date": "1998-11-27",
    "isbn": "ppppppppppppp",
    "price": 1000,
    "stock": 1
}