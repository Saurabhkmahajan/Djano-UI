from django.shortcuts import render

# Create your views here.

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def shop(request):
    context = {}
    return render(request, 'store/shop.html', context)

def about(request):
    context = {}
    return render(request, 'store/about.html', context)

def review(request):
    context = {}
    return render(request, 'store/review.html', context)

def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)