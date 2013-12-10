# Create your views here.
from django.shortcuts import render
from products.forms import *
from products.models import *
from django.http import HttpResponseRedirect

def calculate_rating(id):
    reviews = ProductReview.objects.filter(product_id = id)
    sum_of_ratings = 0.0
    for review in reviews:
        sum_of_ratings = sum_of_ratings + float(review.rating)
    return sum_of_ratings / len(reviews)

def list_products(request):
    products = Product.objects.all().order_by('name')[:20]
    return render(request, 'products/index.html',
        { 'products': products, 'form': AddProductForm() })

def product_page(request, product_id):
    product = Product.objects.get(id = product_id)
    reviews = ProductReview.objects.filter(product_id = product_id)
    return render(request, 'products/product_page.html',
        { 'product': product, 'reviews': reviews, 'form': AddProductReviewForm() })
        
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit = False)
            product.save()
    return HttpResponseRedirect('/products/')

def add_product_review(request, product_id):
    if request.method == 'POST':
        form = AddProductReviewForm(request.POST)
        if form.is_valid():
            product_review = form.save(commit = False)
            product = Product.objects.get(id = product_id)
            product_review.product = product
            product_review.save()
            product.actual_rating = calculate_rating(product_id)
            product.save()
    return HttpResponseRedirect('/products/' + str(product_id))
    
def list_top_products(request):
    top_products = Product.objects.all().order_by('-actual_rating')[:10]
    return render(request, 'products/ranking.html',
        { 'products' : top_products })

def list_worst_products(request):
    worst_products = Product.objects.all().order_by('actual_rating')[:10]
    return render(request, 'products/ranking.html',
        { 'products' : worst_products })