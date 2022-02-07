from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('deposit/', deposit, name="deposit"),
    path('withdraw/', withdraw, name="withdraw"),
    path('showdetails/', showDetails, name="show-details"),
]
