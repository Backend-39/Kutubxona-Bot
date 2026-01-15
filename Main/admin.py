from django.contrib import admin
from .models import *

admin.site.register(
    [
        Talaba,
        Muallif,
        Kitob,
        Kutubxonachi,
        Record
    ]
)
