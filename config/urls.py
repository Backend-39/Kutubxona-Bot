"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home_page),
    path("mualliflar/",mualliflar_view),
    path("mualliflar/<int:muallif_id>/",muallif_info_view),
    path("kitoblar/",kitoblar_view),
    path("kitoblar/<int:kitob_id>/",kitob_info_view),
    path("talabalar/",talabalar_view),
    path("talabalar/<int:talaba_id>/",talaba_info_view),
    path("recordlar/",recordlar_views),
    path("recordlar/<int:record_id>/",record_info_view),
    path("kitoblar/<int:kitob_id>/delete/confirm/",kitob_delete_confirm_view),
    path("kitoblar/<int:kitob_id>/delete/",kitob_delete_view),
    path("mualliflar/<int:muallif_id>/delete/confirm/",muallif_delete_confirm_view),
    path("mualliflar/<int:muallif_id>/delete/",muallif_delete_view),
    path("talabalar/<int:talaba_id>/delete/confirm/",talaba_delete_confirm_view),
    path("talabalar/<int:talaba_id>/delete/",talaba_delete_view),
    path("recordlar/<int:record_id>/delete/confirm/",record_delete_confirm_view),
    path("recordlar/<int:record_id>/delete/",record_delete_view),
    path("kitoblar/add_kitob/",add_kitob_view),
    path("talabalar/add_talaba/",add_talaba_view),
    path("mualliflar/add_muallif/",add_muallif_view),
    path("recordlar/add_record/",add_record_view),
    path("talabalar/<int:talaba_id>/update_page/",talaba_update_page),
    path("talabalar/<int:talaba_id>/update/",talaba_update),
    path("kitoblar/<int:kitob_id>/update_page/",kitob_update_page),
    path("bot/api/", include("api.urls"))
]
