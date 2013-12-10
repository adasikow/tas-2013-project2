# -*- coding: utf-8 -*-
from django.db import models

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
    category = models.CharField(choices = category_choices, default = 'Computer')
    producer = models.CharField(max_length = 30)
    actual_rating = models.FloatField(null = True, blank = True)

class ProductReview(models.Model):
    product = models.ForeignKey(Product)
    author = models.CharField(max_length = 30, null = True, blank = True)
    date = models.DateTimeField(auto_now_add = True)
    rating_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    rating = models.FloatField(choices = rating_choices, default = 5)
    content = models.TextField()