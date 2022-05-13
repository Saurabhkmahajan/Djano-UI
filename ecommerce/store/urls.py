from django.urls import path

from . import views


urlpatterns = [
  #Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('shop/', views.shop, name="shop"),
    path('about/', views.about, name="about"),
    path('review/', views.review, name="review"),
    path('contact/', views.contact, name="contact")

]