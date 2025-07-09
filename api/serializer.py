from books.models import Category,Books,Author
from rest_framework import serializers
from rest_framework.validators import ValidationError

class BooksSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def validate(self, data):
        title = data.get('title',None)
        price = data.get('price',None)

        if not title.isalpha():
            context = {
                'status': False,
                'message': 'Qatelik bar'
            }
            raise ValidationError(context)
        if Books.objects.filter(title=title).exists():
            context = {
                'status' : False,
                'message': 'Onday kitap uje bar'
            }
            raise ValidationError(context)
        if price>2000000 or price<0:
            context = {
                'status': False,
                'message':'Onday cena joq'
            }
            raise ValidationError(context)
        
    def validate_pages(self, data):
            if data<10 or data>5000:
                raise ValidationError({
                    'status' : False,
                    'message' : 'Kitaptin beti onday bomaydi'
                })

class AuthorSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'