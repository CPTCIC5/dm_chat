from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path(r'gc-chat/',ChatConsumer.as_asgi())
]