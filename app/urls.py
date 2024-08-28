
from django.urls import path
from . import views


urlpatterns = [

    path('', views.WalletKeyView.as_view())
   
]


