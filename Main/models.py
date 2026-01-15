from django.db import models

class Talaba(models.Model):
    ism=models.CharField(max_length=50)
    familiya=models.CharField(max_length=50)
    otasining_ismi=models.CharField(max_length=50)
    jinsi=models.CharField(choices=[('erkak','Erkak'),('ayol','Ayol')])
    guruh=models.CharField()
    kurs=models.SmallIntegerField(null=True,blank=True)
    tel=models.CharField(max_length=13,null=True,blank=True)

    class Meta:
        verbose_name_plural="Talabalar"
    
    def __str__(self):
        return f"{self.familiya.capitalize()} {self.ism.capitalize()} {self.otasining_ismi.capitalize()}"

class Muallif(models.Model):
    ism=models.CharField(max_length=50)
    familiya=models.CharField(max_length=50)
    jinsi=models.CharField(choices=[('erkak','Erkak'),('ayol','Ayol')])
    tugilgan_sana=models.DateField(null=True,blank=True)
    tirik=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural="Mualliflar"
    
    def __str__(self):
        return f"{self.familiya.capitalize()} {self.ism.capitalize()}"


class Kitob(models.Model):
    nomi=models.CharField(max_length=255)
    janr=models.CharField(max_length=50)
    sahifa=models.SmallIntegerField()
    muallif=models.ForeignKey(Muallif,on_delete=models.SET_NULL,blank=True,null=True)

    class Meta:
        verbose_name_plural="Kitoblar"
    
    def __str__(self):
        return f"{self.muallif}, {self.nomi} | {self.janr}"
    
class Kutubxonachi(models.Model):
    ism=models.CharField(max_length=50)
    familiya=models.CharField(max_length=50)
    otasining_ismi=models.CharField(max_length=50)
    jinsi=models.CharField(choices=[('erkak','Erkak'),('ayol','Ayol')])
    ish_bosh_vaqti=models.TimeField()
    ish_tug_vaqti=models.TimeField()

    class Meta:
        verbose_name_plural="Kutubxonachilar"
    
    def __str__(self):
        return f"{self.familiya.capitalize()} {self.ism.capitalize()} {self.otasining_ismi.capitalize()}"

class Record(models.Model):
    talaba=models.ForeignKey(Talaba,on_delete=models.SET_NULL,blank=True,null=True)
    kitob=models.ForeignKey(Kitob,on_delete=models.SET_NULL,blank=True,null=True)
    admin=models.ForeignKey(Kutubxonachi,on_delete=models.SET_NULL,blank=True,null=True)
    olingan_sana=models.DateTimeField()
    qaytarish_sana=models.DateField()

    class Meta:
        verbose_name_plural="Recordlar"
    
    def __str__(self):
        return f"{self.kitob} | {self.olingan_sana}"