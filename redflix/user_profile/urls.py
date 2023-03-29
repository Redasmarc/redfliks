from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('shop/', views.shop, name='shop'),
]
