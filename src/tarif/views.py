from rest_framework import viewsets

from .serializers import *


# Create your views here.
class TarifParkirViewSet(viewsets.ModelViewSet):
    queryset = JenisTarif.objects.all()
    serializer_class = JenisTarifSerializer


class MekanismeTarifRuangMilikJalanViewSet(viewsets.ModelViewSet):
    serializer_class = MekanismeTarifRuangMilikJalanSerializer
    queryset = MekanismeTarifRuangMilikJalan.objects.all()


class MekanismeTarifLingkunganViewSet(viewsets.ModelViewSet):
    serializer_class = MekanismeTarifLingkunganSerializer
    queryset = MekanismeTarifLingkungan.objects.all()


class MekanismeTarifPelataranViewSet(viewsets.ModelViewSet):
    serializer_class = MekanismeTarifPelataranSerializer
    queryset = MekanismeTarifPelataran.objects.all()


class MekanismeTarifGedungViewSet(viewsets.ModelViewSet):
    serializer_class = MekanismeTarifGedungSerializer
    queryset = MekanismeTarifGedung.objects.all()


class MekanismeTarifPenitipanKendaraanViewSet(viewsets.ModelViewSet):
    serializer_class = MekanismeTarifPenitipanKendaraanSerializer
    queryset = MekanismeTarifPenitipanKendaraan.objects.all()


class MekanismeTarifParkAndRideViewSet(viewsets.ModelViewSet):
    serializer_class = MekanismeTarifParkAndRideSerializer
    queryset = MekanismeTarifParkAndRide.objects.all()


class MekanismeTarifValletViewSet(viewsets.ModelViewSet):
    serializer_class = MekanismeTarifValletSerializer
    queryset = MekanismeTarifVallet.objects.all()


class MekanismeTarifTPEViewSet(viewsets.ModelViewSet):
    serializer_class = MekanismeTarifTPESerializer
    queryset = MekanismeTarifTPE.objects.all()
