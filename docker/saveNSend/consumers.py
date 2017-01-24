from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user_from_http


# Connected to websocket.connect and websocket.keepalive
@channel_session_user_from_http
def websocket_connect(message):
    print('websocket_connect. message = {}'.format(message))
    # transfer_user(message.http_session, message.channel_session)
    Group("notifications").add(message.reply_channel)

# Connected to websocket.keepalive
@channel_session
def websocket_keepalive(message):
    print('websocket_keepalive. message = {}'.format(message))
    Group("notifications").add(message.reply_channel)


# Connected to websocket.disconnect
@channel_session
def websocket_disconnect(message):
    print('websocket_disconnect. message = {}'.format(message))
    Group("notifications").discard(message.reply_channel)
