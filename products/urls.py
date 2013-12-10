from django.conf.urls import *

urlpatterns = patterns('products.views',
    (r'^$',     'list_products'),
    (r'^(\d+)$', 'product_page'),
    (r'^(\d+)/add_review$', 'add_product_review'),
    (r'^add$', 'add_product'),

)