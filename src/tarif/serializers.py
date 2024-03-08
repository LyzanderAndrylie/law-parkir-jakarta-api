from rest_framework import serializers
from parkir_api.constants import MEKANISME_URL_MAPPING

from .models import *


class MekanismeTarifRuangMilikJalanSerializer(serializers.ModelSerializer):
    jenis_kendaraan = serializers.SlugRelatedField(read_only=True, slug_field='nama', many=True)

    class Meta:
        model = MekanismeTarifRuangMilikJalan
        fields = ['id', 'golongan', 'min_tarif', 'max_tarif', 'cara_pembayaran', 'jenis_tarif', 'jenis_kendaraan']


class MekanismeTarifLingkunganSerializer(serializers.ModelSerializer):
    jenis_kendaraan = serializers.SlugRelatedField(read_only=True, slug_field='nama', many=True)

    class Meta:
        model = MekanismeTarifLingkungan
        fields = ['id', 'mekanisme_harian', 'mekanisme_langganan_umum', 'mekanisme_langganan_khusus', 'jenis_kendaraan']
        depth = 1


class MekanismeTarifPelataranSerializer(serializers.ModelSerializer):
    jenis_kendaraan = serializers.SlugRelatedField(read_only=True, slug_field='nama', many=True)

    class Meta:
        model = MekanismeTarifPelataran
        fields = ['id', 'mekanisme_harian', 'mekanisme_langganan_umum', 'mekanisme_langganan_khusus', 'jenis_kendaraan']
        depth = 1


class MekanismeTarifGedungSerializer(serializers.ModelSerializer):
    jenis_kendaraan = serializers.SlugRelatedField(read_only=True, slug_field='nama', many=True)

    class Meta:
        model = MekanismeTarifGedung
        fields = ['id', 'mekanisme_harian', 'mekanisme_langganan_umum', 'mekanisme_langganan_khusus', 'jenis_kendaraan']
        depth = 1


class MekanismeTarifPenitipanKendaraanSerializer(serializers.ModelSerializer):
    jenis_kendaraan = serializers.SlugRelatedField(read_only=True, slug_field='nama', many=True)

    class Meta:
        model = MekanismeTarifPenitipanKendaraan
        fields = ['id', 'tarif', 'cara_pembayaran', 'jenis_kendaraan']


class MekanismeTarifParkAndRideSerializer(serializers.ModelSerializer):
    jenis_kendaraan = serializers.SlugRelatedField(read_only=True, slug_field='nama', many=True)

    class Meta:
        model = MekanismeTarifParkAndRide
        fields = ['id', 'tarif', 'cara_pembayaran', 'jenis_kendaraan']


class MekanismeTarifValletSerializer(serializers.ModelSerializer):
    class Meta:
        model = MekanismeTarifVallet
        fields = '__all__'


class TarifLanganganSerializer(serializers.ModelSerializer):
    jenis_kendaraan = serializers.SlugRelatedField(read_only=True, slug_field='nama', many=True)

    class Meta:
        model = TarifLanggananTPE
        fields = '__all__'
        depth = 1


class MekanismeTarifTPESerializer(serializers.ModelSerializer):
    tarif_langganan = TarifLanganganSerializer(many=True)

    class Meta:
        model = MekanismeTarifTPE
        fields = ['tarif_harian', 'tarif_langganan']
        depth = 1


class JenisTarifSerializer(serializers.ModelSerializer):
    daftar_mekanisme = serializers.HyperlinkedIdentityField(
        view_name='mekanisme-list',
        lookup_url_kwarg='tarif_pk'
    )

    class Meta:
        model = JenisTarif
        fields = ['nama', 'daftar_mekanisme']

    def to_representation(self, instance):
        request = self.context.get('request')
        url = request.build_absolute_uri('/') + MEKANISME_URL_MAPPING.get(instance.nama)

        return {
            "name": instance.nama,
            'daftar_mekanisme': url
        }
