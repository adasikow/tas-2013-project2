from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def create_new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/products/')
    
    return render(request, 'register.html', {'create_user_form': UserCreationForm()})
    
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username'].encode('UTF-8')
        password = request.POST['password'].encode('UTF-8')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/products/')