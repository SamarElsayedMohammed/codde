from django.urls import path
from .views import OrdersPageView


urlpatterns = [
    path('charge/', charge, name='charge'),
    path('', OrdersPageView.as_view(), name='orders'),
    ]