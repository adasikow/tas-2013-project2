# Django URL configuration, "django-guestbook/guestbook/urls.py"
from django.conf.urls import *

urlpatterns = patterns('guestbook.views',
    (r'^$',     'list_greetings'),
    (r'^sign$', 'create_greeting'),
)