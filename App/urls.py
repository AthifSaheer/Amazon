from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('product-detail-view', ProductDetailView.as_view(), name="productdetailview")
]