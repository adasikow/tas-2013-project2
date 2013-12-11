from django.conf.urls import *

urlpatterns = patterns('accounts.views',
    (r'^create_user$',     'create_new_user'),
    (r'^login$', 'log_in'),
)

urlpatterns += patterns('',
    (r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/',}),
)