# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    """
    >>> service = Service.objects.create(name="remonty", description="uslugi remontowe", performer="budpol")

    # Sprawdzenie domyslnej kategorii oraz oceny
    >>> service.category
    u'building'
    >>> service.actual_rating
    0.0
    """
    name = models.CharField(max_length = 150)
    description = models.TextField()
    category_choices = (
        ('building', 'Budowa, remont'),
        ('kids', 'Dzieci, zwierzęta, opieka'),
        ('education', 'Edukacja, szkolenia'),
        ('company', 'Firma, biuro'),
        ('graphics', 'Grafika, multimedia'),
        ('it', 'Informatyka, telekomunikacja'),
        ('culture', 'Kultura, sztuka'),
        ('marketing', 'Marketing, reklama'),
        ('moto', 'Motoryzacja, transport'),
        ('repair', 'Naprawa, serwis'),
        ('printing', 'Poligrafia'),
        ('housework', 'Prace domowe, ogród'),
        ('law', 'Prawo, finanse'),
        ('entertainment', 'Rozrywka, imprezy'),
        ('craft', 'Rzemiosło, fachowcy'),
        ('sport', 'Sport, turystyka'),
        ('translations', 'Teksty, tłumaczenia'),
        ('health', 'Zdrowie, uroda'),
    )

    @staticmethod
    def category_verbose(category):
        return dict(Service.category_choices)[category]
    
    performer = models.CharField(max_length = 100)
    category = models.CharField(max_length = 30, choices = category_choices, default = 'building')
    actual_rating = models.FloatField(null = True, blank = True, default = 0.0)


class ServiceReview(models.Model):
    service = models.ForeignKey(Service)
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