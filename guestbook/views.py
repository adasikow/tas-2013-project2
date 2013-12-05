# Corresponding Django view, "django-guestbook/guestbook/views.py"
from django.core.cache import cache
from django.shortcuts import render
#from django.views.generic import TemplateView
#from django.views.generic import RedirectView
from guestbook.forms import CreateGreetingForm
from guestbook.models import Greeting
from django.http import HttpResponseRedirect

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
        {'greetings': greetings, 'form': CreateGreetingForm()})
        
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