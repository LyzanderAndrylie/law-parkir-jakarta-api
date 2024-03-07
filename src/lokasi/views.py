from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .filters import LokasiParkirFilter
from .models import LokasiParkir
from .serializers import LokasiParkirListSerializer, LokasiParkirDetailSerializer


# Create your views here.
class LokasiParkirViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LokasiParkir.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['jenis', 'luas_m2', 'kapasitas_mobil', 'kapasitas_motor', 'kapasitas_bus_truk']
    search_fields = ['nama', 'alamat']
    filterset_class = LokasiParkirFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return LokasiParkirListSerializer
        elif self.action == 'retrieve':
            return LokasiParkirDetailSerializer
