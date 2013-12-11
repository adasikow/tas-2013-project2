from django.conf.urls import *
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView

urlpatterns = patterns('',
    (r'^$', RedirectView.as_view(url='/products/')),
    (r'^products/', include('products.urls')),
    (r'^services/', include('services.urls')),
    (r'^guestbook/', include('guestbook.urls')),

    (r'^accounts/create_user/$', 'guestbook.views.create_new_user'),
    (r'^accounts/login/$', 'guestbook.views.log_in'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/guestbook/',}),
)