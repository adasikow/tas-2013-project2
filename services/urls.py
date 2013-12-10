from django.conf.urls import *

urlpatterns = patterns('services.views',
    (r'^$',     'list_services'),
    (r'^(\d+)$', 'service_page'),
    (r'^(\d+)/add_review$', 'add_service_review'),
    (r'^add$', 'add_service'),
    (r'^top$', 'list_top_service'),
    (r'^worst$', 'list_worst_service'),
    (r'^(building|kids|education|company|'
        'graphics|it|games|books|'
        'moto|repair|printing|housework|'
        'law|entertainment|craft|sport|'
        'translations)$', 'list_services_from_category'),
    (r'^(building|kids|education|company|'
        'graphics|it|games|books|'
        'moto|repair|printing|housework|'
        'law|entertainment|craft|sport|'
        'translations)/top$', 'list_top_services'),
    (r'^(building|kids|education|company|'
        'graphics|it|games|books|'
        'moto|repair|printing|housework|'
        'law|entertainment|craft|sport|'
        'translations)/worst$', 'list_worst_services'),
)