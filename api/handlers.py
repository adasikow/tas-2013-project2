from piston.handler import BaseHandler
from products.models import Product

class ProductHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Product
   
    def read(self, request, product_name=None):
        if(product_name):
            return Product.objects.get(name = product_name)
        else:
            return Product.objects.all()