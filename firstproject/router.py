from django.urls import path
from .consumer import *


ws_patterns = [
    path('ws/chat/<str:group_name>',MyConsumer.as_asgi())
]