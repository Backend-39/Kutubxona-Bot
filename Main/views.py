from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import *


def home_page(request):
    return render(request,"index.html")

def mualliflar_view(request):
    filter_value=request.GET.get("filter_value","id")
    search_value=request.GET.get("search_value","")

    if filter_value not in ["id","-id","-ism","ism","-familiya","familiya"]:
        filter_value="id"
    
    mualliflar=Muallif.objects.order_by(filter_value)
    context={
        "mualliflar": mualliflar,
        "search_value": search_value,
        "filter_value": filter_value
    }

    if search_value:
        qidirilgan_mualliflar=Muallif.objects.filter(
            Q(ism__contains=search_value) | 
            Q(familiya__contains=search_value)
        )
        context["qidirilgan_mualliflar"]=qidirilgan_mualliflar
    
    return render(request,"mualliflar.html",context)

def muallif_info_view(request,muallif_id):
    muallif=Muallif.objects.get(id=muallif_id)
    context={
        "muallif": muallif
    }
    return render(request,"muallif_info.html",context)

def kitoblar_view(request):
    search_value=request.GET.get("search_value","")
    filter_value=request.GET.get("filter_value","id")

    if filter_value not in ["id","nomi","-nomi","sahifa","-sahifa"]:
        filter_value="id"
    
    kitoblar=Kitob.objects.order_by(filter_value)
    mualliflar=Muallif.objects.all()

    context={
        "kitoblar": kitoblar,
        "search_value": search_value,
        "filter_value": filter_value,
        "mualliflar": mualliflar
    }
    if search_value:
        qidirilgan_kitoblar=Kitob.objects.filter(nomi__contains=search_value)
        context["searched_books"]=qidirilgan_kitoblar

    return render(request,"kitoblar.html",context)

def kitob_info_view(request,kitob_id):
    kitob=Kitob.objects.get(id=kitob_id)
    context={
        "kitob": kitob
    }
    return render(request,"kitob_info.html",context)

def talabalar_view(request):
    filter_value=request.GET.get("filter_value","id")
    search_value=request.GET.get("search_value","")
    
    if filter_value not in ["id","-id","-ism","ism","-familiya","familiya","kurs","-kurs"]:
        filter_value="id"
    talabalar=Talaba.objects.order_by(filter_value)
    context={
        "talabalar": talabalar,
        "filter_value": filter_value,
        "search_value": search_value
    }

    if search_value:
        qidirilgan_talabalar=Talaba.objects.filter(
            Q(ism__contains=search_value) | 
            Q(familiya__contains=search_value) | 
            Q(otasining_ismi__contains=search_value)
        )
        context["qidirilgan_talabalar"]=qidirilgan_talabalar

    return render(request,"talabalar.html",context)

            

def talaba_info_view(request,talaba_id):
    talaba=Talaba.objects.get(id=talaba_id)
    context={
        "talaba": talaba
    }
    return render(request,"talaba_info.html",context)

def recordlar_views(request):
    talabalar=Talaba.objects.all()
    kitoblar=Kitob.objects.all()
    kutubxonachilar=Kutubxonachi.objects.all()
    recordlar=Record.objects.all()
    context={
        'recordlar': recordlar,
        'talabalar': talabalar,
        'kitoblar': kitoblar,
        'kutubxonachilar': kutubxonachilar
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
        "yes_link": f"/kitoblar/{kitob.id}/delete/",
        "no_link": "/kitoblar/"
    }
    return render(request,"delete_confirm.html",context)

def kitob_delete_view(request,kitob_id):
    kitob=Kitob.objects.get(id=kitob_id)
    kitob.delete()
    return redirect("/kitoblar/")

def muallif_delete_confirm_view(request,muallif_id):
    muallif=Muallif.objects.get(id=muallif_id)
    context={
        "name": f"{muallif.ism} {muallif.familiya}",
        "yes_link": f"/mualliflar/{muallif.id}/delete/",
        "no_link": "/mualliflar/"
    }
    return render(request,"delete_confirm.html",context)

def muallif_delete_view(request,muallif_id):
    muallif=Muallif.objects.get(id=muallif_id)
    muallif.delete()
    return redirect("/mualliflar/")

def talaba_delete_confirm_view(request,talaba_id):
    talaba=Talaba.objects.get(id=talaba_id)
    context={
        "name": f"{talaba.ism} {talaba.familiya} {talaba.otasining_ismi}",
        "yes_link": f"/talabalar/{talaba.id}/delete/",
        "no_link": "/talabalar/"
    }
    return render(request,"delete_confirm.html",context)

def talaba_delete_view(request,talaba_id):
    talaba=Talaba.objects.get(id=talaba_id)
    talaba.delete()
    return redirect("/talabalar/")

def record_delete_confirm_view(request,record_id):
    record=Record.objects.get(id=record_id)
    context={
        "name": f"{record.kitob} | {record.talaba} | {record.admin} | {record.olingan_sana}\n",
        "yes_link": f"/recordlar/{record.id}/delete/",
        "no_link": "/recordlar/"
    }
    return render(request,"delete_confirm.html",context)

def record_delete_view(request,record_id):
    record=Record.objects.get(id=record_id)
    record.delete()
    return redirect("/recordlar/")

def add_kitob_view(request):
    Kitob.objects.create(
        nomi=request.POST.get("nomi"),
        janr=request.POST.get("janr"),
        sahifa=request.POST.get("sahifa"),
        muallif=Muallif.objects.get(id=request.POST.get("muallif_id"))
    )
    return redirect("/kitoblar/")

def add_talaba_view(request):
    Talaba.objects.create(
        ism=request.POST.get("ism"),
        familiya=request.POST.get("familiya"),
        otasining_ismi=request.POST.get("otasining_ismi"),
        jinsi=request.POST.get("jinsi"),
        guruh=request.POST.get("guruh"),
        kurs=request.POST.get("kurs"),
        tel=request.POST.get("tel")
    )
    return redirect("/talabalar/")

def add_muallif_view(request):
    Muallif.objects.create(
        ism=request.POST.get("ism"),
        familiya=request.POST.get("familiya"),
        jinsi=request.POST.get("jinsi"),
        tugilgan_sana=request.POST.get("tugilgan_sana"),
        tirik=True if request.POST.get("tirik")=="yes" else False
    )
    return redirect("/mualliflar/")

def add_record_view(request):
    kitob=Kitob.objects.get(id=request.POST.get("kitob_id"))
    talaba=Talaba.objects.get(id=request.POST.get("talaba_id"))
    kutubxonachi=Kutubxonachi.objects.get(id=request.POST.get("kutubxonachi_id"))
    olingan_sana=request.POST.get("olingan_sana")
    qaytarish_sana=request.POST.get("qaytarish_sana")
    Record.objects.create(
        talaba=talaba,
        kitob=kitob,
        admin=kutubxonachi,
        olingan_sana=olingan_sana,
        qaytarish_sana=qaytarish_sana
    )
    return redirect("/recordlar/")

def talaba_update_page(request,talaba_id):
    talaba=Talaba.objects.get(id=talaba_id)
    context={
        "talaba": talaba
    }
    return render(request,"talaba_update.html",context)

def talaba_update(request,talaba_id):
    talaba=Talaba.objects.get(id=talaba_id)
    talaba.ism=request.POST.get("ism")
    talaba.familiya=request.POST.get("familiya")
    talaba.otasining_ismi=request.POST.get("otasining_ismi")
    talaba.jinsi=request.POST.get("jinsi")
    talaba.guruh=request.POST.get("guruh")
    talaba.kurs=request.POST.get("kurs")
    talaba.tel=request.POST.get("tel")
    talaba.save()
    return redirect(f"/talabalar/{talaba.id}/")

def kitob_update_page(request,kitob_id):
    kitob=Kitob.objects.get(id=kitob_id)
    mualliflar=Muallif.objects.all()
    context={
        "kitob": kitob,
        "mualliflar":mualliflar
    }
    return render(request,"kitob_update.html",context)