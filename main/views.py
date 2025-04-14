from rest_framework import viewsets
from main.models import Category, Info, Contact
from main.serializers import CategorySerializer, InfoSerializer, ContactSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()  # kerak
    serializer_class = InfoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        lang_code = self.request.query_params.get('lang_code')
        if lang_code:
            queryset = queryset.filter(language__lang_code=lang_code)
        return queryset

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
