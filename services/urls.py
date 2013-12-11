from django.conf.urls import *

urlpatterns = patterns('services.views',
    (r'^$',     'list_services'),
    (r'^(\d+)$', 'service_page'),
    (r'^(\d+)/add_review$', 'add_service_review'),
    (r'^add$', 'add_service'),
    (r'^top$', 'list_top_services'),
    (r'^worst$', 'list_worst_services'),
    (r'^(building|kids|education|company|'
        'graphics|it|culture|marketing|'
        'moto|repair|printing|housework|'
        'law|entertainment|craft|sport|'
        'translations|health)$', 'list_services_from_category'),
    (r'^(building|kids|education|company|'
        'graphics|it|culture|marketing|'
        'moto|repair|printing|housework|'
        'law|entertainment|craft|sport|'
        'translations|health)/top$', 'list_top_services'),
    (r'^(building|kids|education|company|'
        'graphics|it|culture|marketing|'
        'moto|repair|printing|housework|'
        'law|entertainment|craft|sport|'
        'translations|health)/worst$', 'list_worst_services'),
)