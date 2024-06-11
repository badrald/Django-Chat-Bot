from django.urls import path

from . import views

urlpatterns = [
    path("", views.chat_bot, name="chat_bot"),
    path("<slug:group_slug>/", views.chat_bot, name="chat_bot_with_group"),
    path(
    "<slug:group_slug>/messages/",
    views.get_chat_messages,
    name="get_chat_messages",
),
]
