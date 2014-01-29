from piston.handler import BaseHandler
from products.models import *
from products.forms import *

class ProductHandler(BaseHandler):
    allowed_methods = ('GET', 'POST',)
    model = Product
   
    def read(self, request, product_name = None):
        if(product_name):
            return Product.objects.get(name = product_name)
        else:
            return Product.objects.all()
    

    def create(self, request, product_name = None, product_desc = None, product_producer = None, product_category = None):
        
        product = None
        if(product_name and product_desc and product_producer): #przekazywanie danych w linku
            product = Product(name = product_name, description = product_desc, producer = product_producer, category = product_category)
        else: # przekazywanie danych POST
            form = AddProductForm(request.POST)
            product = form.save(commit = False)
            #product = Product(name = request.POST['name'], description = request.POST['description'], producer = request.POST['producer'], category = request.POST['category'])
        product.save()
        return product