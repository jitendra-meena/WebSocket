from django.urls import path
from .views import *


urlpatterns = [
    path('register/',Register.as_view(), name='register'),
    path('',Login.as_view(), name='login'),
]
