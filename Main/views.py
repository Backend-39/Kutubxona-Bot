from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

def home_page(request):
    return render(request,"index.html")

def mualliflar_view(request):
    mualliflar=Muallif.objects.all()
    context={
        "mualliflar": mualliflar
    }
    return render(request,"mualliflar.html",context)

def muallif_info_view(request,muallif_id):
    muallif=Muallif.objects.get(id=muallif_id)
    context={
        "muallif": muallif
    }
    return render(request,"muallif_info.html",context)

def kitoblar_view(request):
    kitoblar=Kitob.objects.all()
    context={
        "kitoblar": kitoblar
    }
    return render(request,"kitoblar.html",context)

def kitob_info_view(request,kitob_id):
    kitob=Kitob.objects.get(id=kitob_id)
    context={
        "kitob": kitob
    }
    return render(request,"kitob_info.html",context)

def talabalar_view(request):
    talabalar=Talaba.objects.all()
    context={
        "talabalar": talabalar
    }
    return render(request,"talabalar.html",context)

def talaba_info_view(request,talaba_id):
    talaba=Talaba.objects.get(id=talaba_id)
    context={
        "talaba": talaba
    }
    return render(request,"talaba_info.html",context)

def recordlar_views(request):
    recordlar=Record.objects.all()
    context={
        'recordlar': recordlar
    }
    return render(request,"recordlar.html",context)

def record_info_view(request,record_id):
    record=Record.objects.get(id=record_id)
    context={
        "record": record
    }
    return render(request,"record_info.html",context)

def kitob_delete_confirm_view(request,kitob_id):
    kitob=Kitob.objects.get(id=kitob_id)
    context={
        "name": f"{kitob.nomi}",
        "yes_link": f"/kitoblar/{kitob.id}/delete",
        "no_link": "/kitoblar/"
    }
    return render(request,"delete_confirm.html",context)

def kitob_delete_view(request,kitob_id):
    kitob=Kitob.objects.get(id=kitob_id)
    kitob.delete()
    return redirect("/kitoblar/")
