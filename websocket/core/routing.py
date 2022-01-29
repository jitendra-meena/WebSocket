from django.urls import path
from . import *

websocket_urlpattern = [
  path('wc/chat_sc/',consumers.ChatConsumer.as_asgi()),
  path('wc/chat_ac/',consumers.ChatSyncConsumer.as_asgi()) 
]


