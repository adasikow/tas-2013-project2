from django.conf.urls import *
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView
#from tastypie.api import Api
#from products.api.resources import ProductResource

#v1_api = Api(api_name='v1')
#v1_api.register(ProductResource())

urlpatterns = patterns('',
    (r'^$', RedirectView.as_view(url='/products/')),
    (r'^products/', include('products.urls')),
    (r'^services/', include('services.urls')),
    (r'^accounts/', include('accounts.urls')),
#    (r'^api/', include(v1_api.urls)),
)