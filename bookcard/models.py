from django.db import models


# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    about = models.CharField(max_length=600)
    price = models.IntegerField()
    image = models.ImageField(upload_to='')

    class Meta:
        db_table = "fairy_cards"


class Register(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

    class Meta:
        db_table = "regis_table"
