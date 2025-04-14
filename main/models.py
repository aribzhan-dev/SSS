from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Language(models.Model):
    lang_code = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Info(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)

    title = models.CharField(max_length=200)
    desc = RichTextField(blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Contact(models.Model):
    phone_number = models.CharField(max_length=300)
    whatsapp = models.CharField(max_length=300, blank=True)
    telegram = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.phone_number


