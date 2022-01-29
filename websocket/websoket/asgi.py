"""
ASGI config for websoket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from core.consumers import  *
from django.urls import path
from channels.auth import AuthMiddlewareStack
import core.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websoket.settings')

# # application = get_asgi_application()
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     # Just HTTP for now. (We can add other protocols later.)
# })

# ws_pattern = [
#   path('ws/test/',TestConsumer)
# ]



# application = ProtocolTypeRouter({
#           'websocket':(URLRouter(ws_pattern)
# )
# })    


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket":URLRouter(
                core.routing.websocket_urlpattern
            )
        
    }
)


# application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests

    # WebSocket chat handler
#     "websocket": AuthMiddlewareStack(
#         URLRouter([
#             url(r"^chat/admin/$", AdminChatConsumer.as_asgi()),
#             url(r"^chat/$", PublicChatConsumer.as_asgi()),
#         ])
#     ),
# })


