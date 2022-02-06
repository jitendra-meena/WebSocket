from django.urls import path
from .views import *
urlpatterns = [
  
  path('whatsapp/', Whatsapp.as_view(), name='whatsapp'),
  path('chat/<str:username>/',Chat.as_view(), name='chat'),
]
