# Corresponding Django view, "django-guestbook/guestbook/views.py"
from django.core.cache import cache
from django.shortcuts import render
#from django.views.generic import TemplateView
#from django.views.generic import RedirectView
from guestbook.forms import *
from guestbook.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

"""class DirectTemplateView(TemplateView):
    extra_context = None
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        if self.extra_context is not None:
            for key, value in self.extra_context.items():
                if callable(value):
                    context[key] = value()
                else:
                    context[key] = value
        return context
        """

def list_greetings(request):
    #greetings = cache.get(MEMCACHE_GREETINGS)
    #if greetings is None:
    #    greetings = Greeting.objects.all().order_by('-date')[:10]
    #    cache.add(MEMCACHE_GREETINGS, greetings)
    greetings = Greeting.objects.all().order_by('-date')[:10]
    return render(request, 'guestbook/index.html',
        {'log_in_form': AuthenticationForm(), 'greetings_list': greetings, 'create_greeting_form': CreateGreetingForm(), 'create_user_form': UserCreationForm()})
        
    #return DirectTemplateView.
        
def create_greeting(request):
    # bound form (user input in request)
    if request.method == 'POST':
        form = CreateGreetingForm(request.POST)
        if form.is_valid():
            greeting = form.save(commit=False)
            if request.user.is_authenticated():
                greeting.author = request.user
            greeting.save()
            cache.delete('greetings')
    return HttpResponseRedirect('/guestbook/')
    
def create_new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #username = user.username.encode('UTF-8')
            #password = user.password.encode('UTF-8')
            #user.username = user.username.encode('UTF-8')
            #user.set_password(user.password.encode('UTF-8'))
            #user.email = user.email.encode('UTF-8')
            #user.first_name = user.first_name.encode('UTF-8')
            #user.last_name = user.last_name.encode('UTF-8')
            #user.save()
            #user = authenticate(username=username, password=password)
            #login(request,user)
    return HttpResponseRedirect('/guestbook/')
    
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username'].encode('UTF-8')
        password = request.POST['password'].encode('UTF-8')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/guestbook/')
                