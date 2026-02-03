from django.contrib import admin
from .models import *


@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display=("id","bot_user","ism","familiya","otasining_ismi","jinsi","guruh","kurs","tel")
    list_display_links=("ism",)
    list_filter=("guruh","kurs","jinsi")
    search_fields=("ism","familiya","otasining_ismi")
    list_per_page=50
    list_max_show_all=100
    list_editable=("guruh","kurs","tel")

class KitobInline(admin.StackedInline):
    model=Kitob

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display=("id","ism","familiya")
    list_display_links=("id","ism")
    search_fields=("ism","familiya")
    list_per_page=50
    list_max_show_all=100
    inlines=(KitobInline,)


@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display=("id","nomi","janr","sahifa","muallif")
    list_display_links=("id","nomi")
    list_editable=("janr","sahifa")
    search_fields=("nomi",)
    list_filter=("janr","muallif")
    list_per_page=50
    list_max_show_all=100

class RecordInline(admin.StackedInline):
    model=Record

@admin.register(Kutubxonachi)
class KutubxonachiAdmin(admin.ModelAdmin):
    list_display=("id","ism","familiya","otasining_ismi","jinsi","ish_bosh_vaqti","ish_tug_vaqti")
    list_display_links=("id","ism","familiya")
    list_filter=("ish_bosh_vaqti","ish_tug_vaqti","jinsi")
    search_fields=("ism","familiya","otasining_ismi")
    list_per_page=50
    list_max_show_all=100
    inlines=(RecordInline,)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display=("id","talaba","kitob","admin","olingan_sana","qaytarish_sana")
    list_display_links=("id","talaba")
    list_filter=("talaba","kitob","admin","olingan_sana","qaytarish_sana")
    list_editable=("olingan_sana","qaytarish_sana")
    list_per_page=50
    list_max_show_all=100
    
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display=("id","username")
    list_display_links=("id","username")
    list_per_page=50
    list_max_show_all=100
