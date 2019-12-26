from django.urls import path
from . import views





urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.signinView, name='login'),
    path('logout/', views.signoutView, name='logout'),
    path('search/', views.searchResult, name='search'),
    path('product/<category>/', views.product, name='product'),
    path('detail/<id>/', views.prod_detail, name='detail'),
]
