from django_filters import rest_framework as filters

from .models import LokasiParkir


class LokasiParkirFilter(filters.FilterSet):
    min_luas_m2 = filters.NumberFilter(field_name="luas_m2", lookup_expr='gte')
    max_luas_m2 = filters.NumberFilter(field_name="luas_m2", lookup_expr='lte')
    min_kapasitas_mobil = filters.NumberFilter(field_name="kapasitas_mobil", lookup_expr='gte')
    max_kapasitas_mobil = filters.NumberFilter(field_name="kapasitas_mobil", lookup_expr='lte')
    min_kapasitas_motor = filters.NumberFilter(field_name="kapasitas_motor", lookup_expr='gte')
    max_kapasitas_motor = filters.NumberFilter(field_name="kapasitas_motor", lookup_expr='lte')
    min_kapasitas_bus_truk = filters.NumberFilter(field_name="kapasitas_bus_truk", lookup_expr='gte')
    max_kapasitas_bus_truk = filters.NumberFilter(field_name="kapasitas_bus_truk", lookup_expr='lte')

    class Meta:
        model = LokasiParkir
        fields = ['luas_m2', 'kapasitas_mobil', 'kapasitas_motor', 'kapasitas_bus_truk']