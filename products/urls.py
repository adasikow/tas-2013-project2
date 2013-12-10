from django.conf.urls import *

urlpatterns = patterns('products.views',
    (r'^$',     'list_products'),
    (r'^(\d+)$', 'product_page'),
    (r'^(\d+)/add_review$', 'add_product_review'),
    (r'^add$', 'add_product'),
    (r'^top$', 'list_top_products'),
    (r'^worst$', 'list_worst_products'),
    (r'^(computer|photo|rtv|agd|'
        'office|phones|games|books|'
        'military|house|garden|moto|'
        'sport|clothes|beauty|health|'
        'gifts|jewelry|kids|media|food|'
        'hobby|building)$', 'list_products_from_category'),
    (r'^(computer|photo|rtv|agd|'
        'office|phones|games|books|'
        'military|house|garden|moto|'
        'sport|clothes|beauty|health|'
        'gifts|jewelry|kids|media|food|'
        'hobby|building)/top$', 'list_top_products'),
    (r'^(computer|photo|rtv|agd|'
        'office|phones|games|books|'
        'military|house|garden|moto|'
        'sport|clothes|beauty|health|'
        'gifts|jewelry|kids|media|food|'
        'hobby|building)/worst$', 'list_worst_products'),
)