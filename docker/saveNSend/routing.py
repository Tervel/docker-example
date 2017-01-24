from channels.routing import route

channel_routing = {
    "websocket.connect": "saveNSend.consumers.websocket_connect",
    "websocket.keepalive": "saveNSend.consumers.websocket_keepalive",
    "websocket.disconnect": "saveNSend.consumers.websocket_disconnect"
}
