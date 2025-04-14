from rest_framework import serializers
from .models import Category, Info, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='category.id', read_only=True)
    category_title = serializers.CharField(source='category.title', read_only=True)
    language_id = serializers.IntegerField(source='language.id', read_only=True)
    language_title = serializers.CharField(source='language.title', read_only=True)

    class Meta:
        model = Info
        fields = ['id', 'category_id', 'category_title', 'language_id', 'language_title', 'title', 'desc', 'status']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
