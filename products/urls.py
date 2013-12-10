from django.conf.urls import *

urlpatterns = patterns('products.views',
    (r'^$',     'list_products'),
    (r'^(\d+)$', 'product_page'),
    (r'^(\d+)/add_review$', 'add_product_review'),
    (r'^add$', 'add_product'),
    (r'^top$', 'list_top_products'),
    (r'^worst$', 'list_worst_products'),
)