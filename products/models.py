# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    category_choices = (
        ('computer', 'Komputery'),
        ('photo', 'Foto'),
        ('rtv', 'RTV'),
        ('agd', 'AGD'),
        ('office', 'Biuro'),
        ('phones', 'Telefony'),
        ('games', 'Gry'),
        ('books', 'Książki'),
        ('military', 'Militaria'),
        ('house', 'Dom i Wnętrze'),
        ('garden', 'Ogród i Narzędzia'),
        ('moto', 'Motoryzacja'),
        ('sport', 'Sport'),
        ('clothes', 'Odzież'),
        ('beauty', 'Uroda'),
        ('health', 'Zdrowie'),
        ('gifts', 'Prezenty'),
        ('jewelry', 'Zegarki i biżuteria'),
        ('kids', 'Dla dzieci'),
        ('media', 'Filmy i muzyka'),
        ('food', 'Żywność i napoje'),
        ('hobby', 'Hobby i gadżety'),
        ('building', 'Budowa i remont'),
    )

    @staticmethod
    def category_verbose(category):
        return dict(Product.category_choices)[category]
    
    category = models.CharField(max_length = 30, choices = category_choices, default = 'Computer')
    producer = models.CharField(max_length = 30)
    actual_rating = models.FloatField(null = True, blank = True, default = 0.0)


class ProductReview(models.Model):
    product = models.ForeignKey(Product)
    author = models.ForeignKey(User)
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