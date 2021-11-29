"""
ASGI config for logint2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.urls import path

from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack

from logint2.consumers import NotificationConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logint2.settings')

wspatterns = [
       path('ws/notify/', NotificationConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
     'websocket': AuthMiddlewareStack(
             URLRouter(
                  wspatterns
              )
       )
    # Just HTTP for now. (We can add other protocols later.)
})