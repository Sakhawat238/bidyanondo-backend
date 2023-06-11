from django.urls import path
from .store_api import StoreLogin


urlpatterns = [
    path('store-login/', StoreLogin, name="StoreLogin")
]