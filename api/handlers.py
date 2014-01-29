from piston.handler import BaseHandler
from products.models import Product

class ProductHandler(BaseHandler):
    allowed_methods = ('GET', 'POST',)
    model = Product
   
    def read(self, request, product_name):
        if(product_name):
            return Product.objects.get(name = product_name)
        else:
            return Product.objects.all()
    

    def create(self, request, product_name = None, product_desc = None, product_producer = None, product_category = None):
    
        if(product_name and product_desc and product_producer): #przekazywanie danych w linku
            product = Product(name = product_name, description = product_desc, producer = product_producer, category = product_category)
        else: # przekazywanie danych POST
            product = Product(name = request.name, description = request.description, producer = request.producer, category = request.category)
        product.save()
        return product