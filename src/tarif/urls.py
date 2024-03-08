from django.urls import path, include
from rest_framework import routers
from parkir_api.constants import MEKANISME_URL_MAPPING

from . import views

router = routers.SimpleRouter()
router.register('tarif', views.TarifParkirViewSet, basename='tarif')
router.register(MEKANISME_URL_MAPPING['ruang milik jalan'], views.MekanismeTarifRuangMilikJalanViewSet,
                basename=MEKANISME_URL_MAPPING['ruang milik jalan'])
router.register(MEKANISME_URL_MAPPING['lingkungan'], views.MekanismeTarifLingkunganViewSet,
                basename=MEKANISME_URL_MAPPING['lingkungan'])
router.register(MEKANISME_URL_MAPPING['pelataran'], views.MekanismeTarifPelataranViewSet,
                basename=MEKANISME_URL_MAPPING['pelataran'])
router.register(MEKANISME_URL_MAPPING['gedung'], views.MekanismeTarifGedungViewSet,
                basename=MEKANISME_URL_MAPPING['gedung'])
router.register(MEKANISME_URL_MAPPING['penitipan kendaraan'], views.MekanismeTarifPenitipanKendaraanViewSet,
                basename=MEKANISME_URL_MAPPING['penitipan kendaraan'])
router.register(MEKANISME_URL_MAPPING['park and ride'], views.MekanismeTarifParkAndRideViewSet,
                basename=MEKANISME_URL_MAPPING['park and ride'])
router.register(MEKANISME_URL_MAPPING['vallet'], views.MekanismeTarifValletViewSet,
                basename=MEKANISME_URL_MAPPING['vallet'])
router.register(MEKANISME_URL_MAPPING['terminal parkir elektronik'], views.MekanismeTarifTPEViewSet,
                basename=MEKANISME_URL_MAPPING['terminal parkir elektronik'])

urlpatterns = [
    path('', include(router.urls)),
    path(f'{MEKANISME_URL_MAPPING['ruang milik jalan']}/tarif/', views.HitungTarifRuangMilikJalan.as_view(),
         name="tarif-mekanisme-rumija"),
    path(f'{MEKANISME_URL_MAPPING['lingkungan']}/tarif/', views.HitungTarifLingkungan.as_view(),
         name="tarif-mekanisme-lingkungan"),
    path(f'{MEKANISME_URL_MAPPING['pelataran']}/tarif/', views.HitungTarifPelataran.as_view(),
         name="tarif-mekanisme-pelataran"),
    path(f'{MEKANISME_URL_MAPPING['gedung']}/tarif/', views.HitungTarifGedung.as_view(),
         name="tarif-mekanisme-gedung"),
    path(f'{MEKANISME_URL_MAPPING['penitipan kendaraan']}/tarif/', views.HitungTarifPenitipan.as_view(),
         name="tarif-mekanisme-penitipan"),
]
