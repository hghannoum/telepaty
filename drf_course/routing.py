
# routing.py
# myproject/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from core.routing import websocket_urlpatterns  # Import the websocket_urlpatterns

application = ProtocolTypeRouter({
     "websocket": 
        URLRouter(websocket_urlpatterns),  # Use the imported websocket_urlpatterns
})
