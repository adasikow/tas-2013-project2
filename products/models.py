# -*- coding: utf-8 -*-
from django.db import models
from decimal import *

class Product(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    category_choices = (
        ('Computer', 'Komputery'),
        ('Photo', 'Foto'),
        ('RTV', 'RTV'),
        ('AGD', 'AGD'),
        ('Office', 'Biuro'),
        ('Phones', 'Telefony'),
        ('Games', 'Gry'),
        ('Books', 'Książki'),
        ('Military', 'Militaria'),
        ('House', 'Dom i Wnętrze'),
        ('Garden', 'Ogród i Narzędzia'),
        ('Moto', 'Motoryzacja'),
        ('Sport', 'Sport'),
        ('Clothes', 'Odzież'),
        ('Beauty', 'Uroda'),
        ('Health', 'Zdrowie'),
        ('Gifts', 'Prezenty'),
        ('Jewelry', 'Zegarki i biżuteria'),
        ('Kids', 'Dla dzieci'),
        ('Media', 'Filmy i muzyka'),
        ('Food', 'Żywność i napoje'),
        ('Hobby', 'Hobby i gadżety'),
        ('Building', 'Budowa i remont'),
    )
    category = models.CharField(max_length = 30, choices = category_choices, default = 'Computer')
    producer = models.CharField(max_length = 30)
    #actual_rating = models.DecimalField(null = True, blank = True, default = Decimal((0, (0, 0), -1)), max_digits = 10, decimal_places = 2)
    actual_rating = models.FloatField(null = True, blank = True, default = 0.0)

class ProductReview(models.Model):
    product = models.ForeignKey(Product)
    author = models.CharField(max_length = 30, null = True, blank = True)
    date = models.DateTimeField(auto_now_add = True)
    rating_choices = (
        (1.0, 1),
        (2.0, 2),
        (3.0, 3),
        (4.0, 4),
        (5.0, 5),
        (6.0, 6),
        (7.0, 7),
        (8.0, 8),
        (9.0, 9),
        (10.0, 10),
    )
    #rating = models.DecimalField(choices = rating_choices, default = 5)
    rating = models.FloatField(choices = rating_choices, default = 5.0)
    content = models.TextField()