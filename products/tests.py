from django.test import TestCase
from django.contrib.auth.models import User
from products.models import *
from products.views import calculate_rating

class ProductReviewTest(TestCase):
    def setUp(self):
        product = Product(name = "A10-7850", description = "Kaveri APU", producer = "AMD")
        user = User(username = "jan")
        user.set_password("kowalski")
        product.save()
        user.save()
        ProductReview.objects.create(product = product, author = user, content = "ok")
        
        
    def test_calculate_rating(self):
        """
        Sprawdza, czy domyslna ocena w recenzji produktu to 5.0 oraz czy poprawnie dziala obliczanie oceny produktu
        """
        product = Product.objects.get(name = "A10-7850")
        self.assertEqual(calculate_rating(product.id), 4.0)
        