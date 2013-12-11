from django.shortcuts import render
from services.forms import *
from services.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

def calculate_rating(id):
    reviews = ServiceReview.objects.filter(service_id = id)
    sum_of_ratings = 0.0
    for review in reviews:
        sum_of_ratings = sum_of_ratings + float(review.rating)
    return sum_of_ratings / len(reviews)

def list_services(request):
    services = Service.objects.all().order_by('name')[:20]
    return render(request, 'services/ranking.html',
        { 'log_in_form': AuthenticationForm(), 'services': services })

def list_services_from_category(request, category):
    services = Service.objects.filter(category = category).order_by('name')[:20]
    return render(request, 'services/category.html',
        { 'log_in_form': AuthenticationForm(), 'services': services, 'category': category })

def service_page(request, service_id):
    service = Service.objects.get(id = service_id)
    reviews = ServiceReview.objects.filter(service_id = service_id)
    return render(request, 'services/service_page.html',
        { 'log_in_form': AuthenticationForm(), 'service': service, 'reviews': reviews, 'form': AddServiceReviewForm() })
        
def add_service(request):
    if request.method == 'POST':
        form = AddServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit = False)
            service.save()
    return render(request, 'services/add_service.html',
        { 'add_service_form': AddServiceForm() })

def add_service_review(request, service_id):
    if request.method == 'POST':
        form = AddServiceReviewForm(request.POST)
        if form.is_valid():
            service_review = form.save(commit = False)
            service = Service.objects.get(id = service_id)
            service_review.service = service
            service_review.author = request.user
            service_review.save()
            service.actual_rating = calculate_rating(service_id)
            service.save()
    return HttpResponseRedirect('/services/' + str(service_id))

def list_top_services(request, category = None):
    if(category is None):
        top_services = Service.objects.all().order_by('-actual_rating')[:10]
    else:
        top_services = Service.objects.filter(category = category).order_by('-actual_rating')[:10]
    return render(request, 'services/ranking.html',
        { 'log_in_form': AuthenticationForm(), 'services' : top_services })

def list_worst_services(request, category = None):
    if(category is None):
        worst_services = Service.objects.all().order_by('actual_rating')[:10]
    else:
        worst_services = Service.objects.filter(category = category).order_by('actual_rating')[:10]
    return render(request, 'services/ranking.html',
        { 'log_in_form': AuthenticationForm(), 'services' : worst_services })
