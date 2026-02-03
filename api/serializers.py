from Main.models import Kitob, Talaba, BotUser, Muallif
from rest_framework.serializers import ModelSerializer

class BotUserSerializer(ModelSerializer):
    class Meta:
        model=BotUser
        fields="__all__"

class TalabaSerializer(ModelSerializer):
    class Meta:
        model=Talaba
        fields="__all__"

class MuallifSerializer(ModelSerializer):
    class Meta:
        model=Muallif
        fields=("ism","familiya")

class KitobSerializer(ModelSerializer):
    muallif=MuallifSerializer(read_only=True)
    class Meta:
        model=Kitob
        fields="__all__"