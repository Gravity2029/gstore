from django.urls import path
from . import views

app_name = 'gmain'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('catalog', views.CatalogView.as_view(), name='catalog_all'),
    path('catalog/<slug:categor_slug>/', views.CatalogView.as_view(), name='catalog'),
    path('product/<slug:slug>', views.ProductView.as_view(), name='product_detail'),
]