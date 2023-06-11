from django.urls import path
from .store_api import StoreLogin
from .qr_api import QrSearch


urlpatterns = [
    path('store-login/', StoreLogin, name="StoreLogin"),
    path('qr-search/', QrSearch, name="QrSearch")
]