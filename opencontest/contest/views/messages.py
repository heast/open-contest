import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from contest.auth import logged_in_required
from contest.models.message import Message
from contest.models.user import User
from contest import register
from contest.UIElements.lib.htmllib import html_encode


@logged_in_required
def getMessages(request):
    timestamp = float(request.POST["timestamp"])
    user = User.get(request.COOKIES['user'])
    newTime = time.time() * 1000
    messages = Message.messagesSince(timestamp)
    applicable = [message.toJSON() for message in messages if
                  (message.toUser and message.toUser.id == user.id) or message.isGeneral or (
                              message.isAdmin and user.isAdmin()) or message.fromUser.id == user.id]
    applicable = sorted(applicable, key=lambda msg: msg["timestamp"], reverse=True)
    return JsonResponse({
        "messages": applicable,
        "timestamp": newTime
    })


@logged_in_required
def sendMessage(params, setHeader, user):
    message = Message()
    message.fromUser = user
    message.message = html_encode(params["message"])
    message.timestamp = time.time() * 1000
    if user.isAdmin():
        message.toUser = User.get(params["to"])
        message.isGeneral = params["to"] == "general"
        message.replyTo = params.get("replyTo")
    else:
        message.isAdmin = True
    message.save()
    return "ok"

#
# # TODO: move to urls
# # register.post("/getMessages", "loggedin", getMessages, True)
# register.post("/sendMessage", "loggedin", sendMessage)
