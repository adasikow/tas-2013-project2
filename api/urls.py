from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import *

class CsrfExemptResource( Resource ):
    def __init__( self, handler, authentication = None ):
        super( CsrfExemptResource, self ).__init__( handler, authentication )
        self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

product_handler = CsrfExemptResource( ProductHandler )

urlpatterns = patterns('',
    (r'^product$', product_handler),
    (r'^product/(?P<product_name>.*)/(?P<product_desc>.*)/(?P<product_producer>.*)/(?P<product_category>.*)$', product_handler),
    (r'^products$', product_handler),
)