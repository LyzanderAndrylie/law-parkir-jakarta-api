import re

from rest_framework import serializers

from .models import LokasiParkir


class LokasiParkirDetailSerializer(serializers.ModelSerializer):
    daftar_lokasi_parkir = serializers.SerializerMethodField()

    class Meta:
        model = LokasiParkir
        fields = ['periode_data', 'nama', 'jenis', 'alamat', 'luas_m2', 'kapasitas_mobil', 'kapasitas_motor',
                  'kapasitas_bus_truk', 'daftar_lokasi_parkir']

    def get_daftar_lokasi_parkir(self, obj):
        request = self.context.get('request')
        daftar_lokasi_parkir_detail_url = request.build_absolute_uri()
        daftar_lokasi_parkir_url = re.sub(r'/\d+/', '/', daftar_lokasi_parkir_detail_url)
        return daftar_lokasi_parkir_url


class LokasiParkirListSerializer(serializers.ModelSerializer):
    detail_lokasi_parkir = serializers.HyperlinkedIdentityField(view_name='lokasi-parkir-detail')

    class Meta:
        model = LokasiParkir
        fields = ['periode_data', 'nama', 'jenis', 'alamat', 'luas_m2', 'kapasitas_mobil', 'kapasitas_motor',
                  'kapasitas_bus_truk', 'detail_lokasi_parkir']
