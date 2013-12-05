from django.conf.urls.defaults import *
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView

urlpatterns = patterns('',
    (r'^$', RedirectView.as_view(url='/guestbook/')),
    (r'^guestbook/', include('guestbook.urls')),

    # auth specific urls
	# nie dziala
    #(r'^accounts/create_user/$', 'guestbook.views.create_new_user'),
    #(r'^accounts/login/$', 'django.contrib.auth.views.login',
    #    {'authentication_form': AuthenticationForm,
    #    'template_name': 'guestbook/login.html',}),
    #(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
    #    {'next_page': '/guestbook/',}),
)