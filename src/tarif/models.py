from django.db import models

from parkir_api.constants import (
    JENIS_PARKIR, JENIS_GOLONGAN_RUMIJA, JENIS_KENDARAAN, CARA_PEMBAYARAN,
    JENIS_PENGGUNAAN_LAHAN)


# Create your models here.
class JenisTarif(models.Model):
    nama = models.CharField(choices=JENIS_PARKIR)


class MekanismeTarif(models.Model):
    jenis_tarif = models.ForeignKey(JenisTarif, on_delete=models.CASCADE, related_name="mekanisme")
    # nama = models.CharField(max_length=100)


class Kendaraan(models.Model):
    nama = models.CharField(choices=JENIS_KENDARAAN)


class MekanismeTarifRuangMilikJalan(MekanismeTarif):
    golongan = models.CharField(choices=JENIS_GOLONGAN_RUMIJA)
    jenis_kendaraan = models.ManyToManyField(Kendaraan)
    min_tarif = models.IntegerField()
    max_tarif = models.IntegerField()
    cara_pembayaran = models.CharField(choices=CARA_PEMBAYARAN)


class MekanismeTarifHarian(models.Model):
    min_tarif_jam_pertama = models.IntegerField()
    max_tarif_jam_pertama = models.IntegerField()
    min_tarif_jam_berikutnya = models.IntegerField()
    max_tarif_jam_berikutnya = models.IntegerField()
    cara_pembayaran = models.CharField(choices=CARA_PEMBAYARAN)


class MekanismeTarifLanggananUmum(models.Model):
    hari = models.IntegerField()
    intensitas = models.IntegerField()
    min_tarif_dasar = models.IntegerField()
    max_tarif_dasar = models.IntegerField()


class MekanismeTarifLanggananKhusus(models.Model):
    hari = models.IntegerField()
    kali_parkir = models.IntegerField()
    min_tarif_dasar = models.IntegerField()
    max_tarif_dasar = models.IntegerField()
    multiplier = models.FloatField()


class MekanismeTarifLingkungan(MekanismeTarif):
    jenis_kendaraan = models.ManyToManyField(Kendaraan)
    mekanisme_harian = models.OneToOneField(MekanismeTarifHarian, on_delete=models.CASCADE)
    mekanisme_langganan_umum = models.OneToOneField(MekanismeTarifLanggananUmum, on_delete=models.CASCADE)
    mekanisme_langganan_khusus = models.OneToOneField(MekanismeTarifLanggananKhusus, on_delete=models.CASCADE)


class MekanismeTarifPelataran(MekanismeTarif):
    jenis_kendaraan = models.ManyToManyField(Kendaraan)
    mekanisme_harian = models.OneToOneField(MekanismeTarifHarian, on_delete=models.CASCADE)
    mekanisme_langganan_umum = models.OneToOneField(MekanismeTarifLanggananUmum, on_delete=models.CASCADE)
    mekanisme_langganan_khusus = models.OneToOneField(MekanismeTarifLanggananKhusus, on_delete=models.CASCADE)


class MekanismeTarifGedung(MekanismeTarif):
    jenis_kendaraan = models.ManyToManyField(Kendaraan)
    mekanisme_harian = models.OneToOneField(MekanismeTarifHarian, on_delete=models.CASCADE)
    mekanisme_langganan_umum = models.OneToOneField(MekanismeTarifLanggananUmum, on_delete=models.CASCADE)
    mekanisme_langganan_khusus = models.OneToOneField(MekanismeTarifLanggananKhusus, on_delete=models.CASCADE)


class MekanismeTarifPenitipanKendaraan(MekanismeTarif):
    jenis_kendaraan = models.ManyToManyField(Kendaraan)
    tarif = models.IntegerField()
    cara_pembayaran = models.CharField(choices=CARA_PEMBAYARAN)


class MekanismeTarifParkAndRide(MekanismeTarif):
    jenis_kendaraan = models.ManyToManyField(Kendaraan)
    tarif = models.IntegerField()
    cara_pembayaran = models.CharField(choices=CARA_PEMBAYARAN)


class MekanismeTarifVallet(MekanismeTarif):
    min_tarif = models.IntegerField()
    max_tarif = models.IntegerField()


class MekanismeTarifTPE(MekanismeTarif):
    tarif_harian = models.OneToOneField(JenisTarif, on_delete=models.CASCADE)


class JenisLanggananTPE(models.Model):
    jam = models.IntegerField()
    jenis_penggunaan_lahan_parkir = models.CharField(choices=JENIS_PENGGUNAAN_LAHAN)


class TarifLanggananTPE(models.Model):
    tarif_tpe = models.ForeignKey(MekanismeTarifTPE, on_delete=models.CASCADE, related_name="tarif_langganan")
    jenis_langganan_per_hari = models.ManyToManyField(JenisLanggananTPE, related_name='tpe')
    jenis_kendaraan = models.ManyToManyField(Kendaraan)
    total_hari = models.IntegerField()
    tarif_hari_jam = models.IntegerField()
