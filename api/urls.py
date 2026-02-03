from django.urls import path
from .views import *

urlpatterns=[
    path("bot-users/",BotUsersApiView.as_view()),
    path("bot-users/<int:telegram_id>/",BotUserInfoApiView.as_view()),
    path("bot-users/infos/",TalabaApiView.as_view()),
    path("bot-users/infos/<int:telegram_id>/",TalabaInfoApiView.as_view()),
    path("kitoblar/",KitobApiView.as_view())
]