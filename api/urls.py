from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import *

product_handler = Resource(ProductHandler)

urlpatterns = patterns('',
   (r'^product$', product_handler),
   (r'^products$', product_handler),
)