from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', login_required(views.product_table), name='product_table'),
    path('asajax/', views.product_as_json, name='product_as_json'),
]
