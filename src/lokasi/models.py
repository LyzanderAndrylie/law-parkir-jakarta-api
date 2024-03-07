from django.db import models

from parkir_api.constants import JENIS_PARKIR


# Create your models here.
class LokasiParkir(models.Model):
    periode_data = models.CharField(max_length=4)
    nama = models.CharField(max_length=100)
    jenis = models.CharField(choices=JENIS_PARKIR)
    alamat = models.CharField(max_length=100)
    luas_m2 = models.IntegerField()
    kapasitas_mobil = models.IntegerField()
    kapasitas_motor = models.IntegerField()
    kapasitas_bus_truk = models.IntegerField()
