from django.shortcuts import render
from Main.models import BotUser,Talaba,Kitob
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

class BotUsersApiView(ListCreateAPIView):
    queryset=BotUser.objects.all()
    serializer_class=BotUserSerializer

class BotUserInfoApiView(RetrieveAPIView):
    queryset=BotUser.objects.all()
    serializer_class=BotUserSerializer
    lookup_field="id"
    lookup_url_kwarg="telegram_id"

class TalabaInfoApiView(RetrieveAPIView):
    queryset=Talaba.objects.all()
    serializer_class=TalabaSerializer
    lookup_field="bot_user"
    lookup_url_kwarg="telegram_id"

class TalabaApiView(ListCreateAPIView):
    queryset=Talaba.objects.all()
    serializer_class=TalabaSerializer

class KitobApiView(ListCreateAPIView):
    queryset=Kitob.objects.all()
    serializer_class=KitobSerializer


