from django.shortcuts import render
from products.forms import *
from products.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

def calculate_rating(id):
    reviews = ProductReview.objects.filter(product_id = id)
    sum_of_ratings = 0.0
    for review in reviews:
        sum_of_ratings = sum_of_ratings + float(review.rating)
    return sum_of_ratings / len(reviews)

def list_products(request):
    products = Product.objects.all().order_by('name')[:20]
    return render(request, 'products/ranking.html',
        { 'log_in_form': AuthenticationForm(), 'products': products})
        
def list_products_from_category(request, category):
    products = Product.objects.filter(category = category).order_by('name')[:20]
    return render(request, 'products/category.html',
        { 'log_in_form': AuthenticationForm(), 'products': products, 'category': category })

def product_page(request, product_id):
    product = Product.objects.get(id = product_id)
    reviews = ProductReview.objects.filter(product_id = product_id)
    return render(request, 'products/product_page.html',
        { 'log_in_form': AuthenticationForm(), 'product': product, 'reviews': reviews, 'form': AddProductReviewForm() })
        
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit = False)
            product.save()
    return render(request, 'products/add_product.html',
        { 'add_product_form': AddProductForm() })

def add_product_review(request, product_id):
    if request.method == 'POST':
        form = AddProductReviewForm(request.POST)
        if form.is_valid():
            product_review = form.save(commit = False)
            product = Product.objects.get(id = product_id)
            product_review.product = product
            product_review.author = request.user
            product_review.save()
            product.actual_rating = calculate_rating(product_id)
            product.save()
    return HttpResponseRedirect('/products/' + str(product_id))
    
def list_top_products(request, category = None):
    if(category is None):
        top_products = Product.objects.all().order_by('-actual_rating')[:10]
    else:
        top_products = Product.objects.filter(category = category).order_by('-actual_rating')[:10]
    return render(request, 'products/ranking.html',
        { 'log_in_form': AuthenticationForm(), 'products' : top_products })

def list_worst_products(request, category = None):
    if(category is None):
        worst_products = Product.objects.all().order_by('actual_rating')[:10]
    else:
        worst_products = Product.objects.filter(category = category).order_by('actual_rating')[:10]
    return render(request, 'products/ranking.html',
        {'log_in_form': AuthenticationForm(), 'products' : worst_products })
