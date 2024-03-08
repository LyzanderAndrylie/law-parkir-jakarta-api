from rest_framework import viewsets, status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *


# Create your views here.
class TarifParkirViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JenisTarif.objects.all()
    serializer_class = JenisTarifSerializer


class MekanismeTarifRuangMilikJalanViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MekanismeTarifRuangMilikJalanSerializer
    queryset = MekanismeTarifRuangMilikJalan.objects.all()
    lookup_value_regex = r'\d+'


class MekanismeTarifLingkunganViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MekanismeTarifLingkunganSerializer
    queryset = MekanismeTarifLingkungan.objects.all()
    lookup_value_regex = r'\d+'


class MekanismeTarifPelataranViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MekanismeTarifPelataranSerializer
    queryset = MekanismeTarifPelataran.objects.all()
    lookup_value_regex = r'\d+'


class MekanismeTarifGedungViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MekanismeTarifGedungSerializer
    queryset = MekanismeTarifGedung.objects.all()
    lookup_value_regex = r'\d+'


class MekanismeTarifPenitipanKendaraanViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MekanismeTarifPenitipanKendaraanSerializer
    queryset = MekanismeTarifPenitipanKendaraan.objects.all()
    lookup_value_regex = r'\d+'


class MekanismeTarifParkAndRideViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MekanismeTarifParkAndRideSerializer
    queryset = MekanismeTarifParkAndRide.objects.all()


class MekanismeTarifValletViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MekanismeTarifValletSerializer
    queryset = MekanismeTarifVallet.objects.all()


class MekanismeTarifTPEViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MekanismeTarifTPESerializer
    queryset = MekanismeTarifTPE.objects.all()


class HitungTarifRuangMilikJalan(APIView):
    def get(self, request):
        golongan = request.query_params.get('golongan', '')
        jam = request.query_params.get('jam', '')
        kendaraan = request.query_params.get('kendaraan', '')

        if not (golongan and jam and kendaraan):
            return Response({
                "error": "Query parameter is missing"
            }, status=status.HTTP_400_BAD_REQUEST)

        if golongan not in ['kpp', 'a', 'b']:
            return Response({
                "error": "Golongan is wrong (Option: kpp | a | b)"
            }, status=status.HTTP_400_BAD_REQUEST)

        if not jam.isdigit() or int(jam) < 0:
            return Response({
                "error": "Jam is not a number"
            }, status=status.HTTP_400_BAD_REQUEST)

        if kendaraan not in ['sedan', 'jeep', 'minibus', 'pickup', 'bus', 'truk', 'sepeda motor', 'sepeda']:
            return Response({
                "error": "Kendaraan is wrong (Option: sedan | jeep | minibus | pickup | bus | truk | sepeda motor | sepeda)"
            }, status=status.HTTP_400_BAD_REQUEST)

        jam = int(jam)

        tipe_golongan = {
            "kpp": "jalan kawasan pengendalian parkir (KPP)",
            "a": "jalan A",
            "b": "jalan B"
        }

        mekanisme = MekanismeTarifRuangMilikJalan.objects.get(golongan=tipe_golongan[golongan],
                                                              jenis_kendaraan__nama=kendaraan)

        if mekanisme.cara_pembayaran == "per jam":
            sisa_jam = 0 if (jam - 1) < 0 else jam - 1
            min_total_tarif = mekanisme.min_tarif + mekanisme.min_tarif * sisa_jam
            max_total_tarif = mekanisme.max_tarif + mekanisme.max_tarif * sisa_jam
            avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

            return Response({
                "golongan": mekanisme.golongan,
                "cara_pembayaran": mekanisme.cara_pembayaran,
                "min_total_tarif": min_total_tarif,
                "max_total_tarif": max_total_tarif,
                "avg_total_tarif": avg_total_tarif,
            }, status=status.HTTP_200_OK)
        elif mekanisme.cara_pembayaran == "satu kali parkir":
            min_total_tarif = mekanisme.min_tarif
            max_total_tarif = mekanisme.max_tarif
            avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

            return Response({
                "golongan": mekanisme.golongan,
                "cara_pembayaran": mekanisme.cara_pembayaran,
                "min_total_tarif": min_total_tarif,
                "max_total_tarif": max_total_tarif,
                "avg_total_tarif": avg_total_tarif,
            }, status=status.HTTP_200_OK)


class HitungTarifLingkungan(APIView):

    def get(self, request):
        jenis = request.query_params.get('jenis', '')
        jam = request.query_params.get('jam', '')
        kendaraan = request.query_params.get('kendaraan', '')

        if not (jenis and jam and kendaraan):
            return Response({
                "error": "Query parameter is missing"
            }, status=status.HTTP_400_BAD_REQUEST)

        if jenis not in ['harian', 'langganan_umum', 'langganan_khusus']:
            return Response({
                "error": "Jenis is wrong (Option: harian | langganan_umum | langganan_khusus)"
            }, status=status.HTTP_400_BAD_REQUEST)

        if not jam.isdigit() or int(jam) < 0:
            return Response({
                "error": "Jam is not valid"
            }, status=status.HTTP_400_BAD_REQUEST)

        if kendaraan not in ['sedan', 'jeep', 'minibus', 'pickup', 'bus', 'truk', 'sepeda motor', 'sepeda']:
            return Response({
                "error": "Kendaraan is wrong (Option: sedan | jeep | minibus | pickup | bus | truk | sepeda motor | sepeda)"
            }, status=status.HTTP_400_BAD_REQUEST)

        jam = int(jam)

        tipe_mekanisme = {
            "harian": "mekanisme_harian",
            "langganan_umum": "mekanisme_langganan_umum",
            "langganan_khusus": "mekanisme_langganan_khusus"
        }

        mekanisme = MekanismeTarifLingkungan.objects.get(jenis_kendaraan__nama=kendaraan)
        jenis_mekanisme = tipe_mekanisme[jenis]
        ketentuan_mekanisme = getattr(mekanisme, jenis_mekanisme)

        if jenis_mekanisme == 'mekanisme_harian':
            if ketentuan_mekanisme.cara_pembayaran == 'per jam':
                sisa_jam = 0 if (jam - 1) < 0 else jam - 1
                min_total_tarif = ketentuan_mekanisme.min_tarif_jam_pertama + ketentuan_mekanisme.min_tarif_jam_berikutnya * sisa_jam
                max_total_tarif = ketentuan_mekanisme.max_tarif_jam_pertama + ketentuan_mekanisme.max_tarif_jam_berikutnya * sisa_jam
                avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

                return Response({
                    "cara_pembayaran": ketentuan_mekanisme.cara_pembayaran,
                    "min_total_tarif": min_total_tarif,
                    "max_total_tarif": max_total_tarif,
                    "avg_total_tarif": avg_total_tarif,
                }, status=status.HTTP_200_OK)
            elif ketentuan_mekanisme.cara_pembayaran == 'satu kali parkir':
                min_total_tarif = ketentuan_mekanisme.min_tarif_jam_pertama
                max_total_tarif = ketentuan_mekanisme.max_tarif_jam_pertama
                avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

                return Response({
                    "cara_pembayaran": ketentuan_mekanisme.cara_pembayaran,
                    "min_total_tarif": min_total_tarif,
                    "max_total_tarif": max_total_tarif,
                    "avg_total_tarif": avg_total_tarif,
                }, status=status.HTTP_200_OK)
        elif jenis_mekanisme == 'mekanisme_langganan_umum':
            min_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.intensitas * ketentuan_mekanisme.min_tarif_dasar
            max_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.intensitas * ketentuan_mekanisme.max_tarif_dasar
            avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

            return Response({
                "jenis_mekanisme": jenis_mekanisme,
                "min_total_tarif": min_total_tarif,
                "max_total_tarif": max_total_tarif,
                "avg_total_tarif": avg_total_tarif,
            }, status=status.HTTP_200_OK)

        elif jenis_mekanisme == 'mekanisme_langganan_khusus':
            min_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.kali_parkir * ketentuan_mekanisme.min_tarif_dasar * ketentuan_mekanisme.multiplier
            max_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.kali_parkir * ketentuan_mekanisme.max_tarif_dasar * ketentuan_mekanisme.multiplier
            avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

            return Response({
                "jenis_mekanisme": jenis_mekanisme,
                "min_total_tarif": min_total_tarif,
                "max_total_tarif": max_total_tarif,
                "avg_total_tarif": avg_total_tarif,
            }, status=status.HTTP_200_OK)


class HitungTarifPelataran(APIView):

    def get(self, request):
        jenis = request.query_params.get('jenis', '')
        jam = request.query_params.get('jam', '')
        kendaraan = request.query_params.get('kendaraan', '')

        if not (jenis and jam and kendaraan):
            return Response({
                "error": "Query parameter is missing"
            }, status=status.HTTP_400_BAD_REQUEST)

        if jenis not in ['harian', 'langganan_umum', 'langganan_khusus']:
            return Response({
                "error": "Jenis is wrong (Option: harian | langganan_umum | langganan_khusus)"
            }, status=status.HTTP_400_BAD_REQUEST)

        if not jam.isdigit() or int(jam) < 0:
            return Response({
                "error": "Jam is not valid"
            }, status=status.HTTP_400_BAD_REQUEST)

        if kendaraan not in ['sedan', 'jeep', 'minibus', 'pickup', 'bus', 'truk', 'sepeda motor', 'sepeda']:
            return Response({
                "error": "Kendaraan is wrong (Option: sedan | jeep | minibus | pickup | bus | truk | sepeda motor | sepeda)"
            }, status=status.HTTP_400_BAD_REQUEST)

        jam = int(jam)

        tipe_mekanisme = {
            "harian": "mekanisme_harian",
            "langganan_umum": "mekanisme_langganan_umum",
            "langganan_khusus": "mekanisme_langganan_khusus"
        }

        mekanisme = MekanismeTarifPelataran.objects.get(jenis_kendaraan__nama=kendaraan)
        jenis_mekanisme = tipe_mekanisme[jenis]
        ketentuan_mekanisme = getattr(mekanisme, jenis_mekanisme)

        if jenis_mekanisme == 'mekanisme_harian':
            if ketentuan_mekanisme.cara_pembayaran == 'per jam':
                sisa_jam = 0 if (jam - 1) < 0 else jam - 1
                min_total_tarif = ketentuan_mekanisme.min_tarif_jam_pertama + ketentuan_mekanisme.min_tarif_jam_berikutnya * sisa_jam
                max_total_tarif = ketentuan_mekanisme.max_tarif_jam_pertama + ketentuan_mekanisme.max_tarif_jam_berikutnya * sisa_jam
                avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

                return Response({
                    "cara_pembayaran": ketentuan_mekanisme.cara_pembayaran,
                    "min_total_tarif": min_total_tarif,
                    "max_total_tarif": max_total_tarif,
                    "avg_total_tarif": avg_total_tarif,
                }, status=status.HTTP_200_OK)
            elif ketentuan_mekanisme.cara_pembayaran == 'satu kali parkir':
                min_total_tarif = ketentuan_mekanisme.min_tarif_jam_pertama
                max_total_tarif = ketentuan_mekanisme.max_tarif_jam_pertama
                avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

                return Response({
                    "cara_pembayaran": ketentuan_mekanisme.cara_pembayaran,
                    "min_total_tarif": min_total_tarif,
                    "max_total_tarif": max_total_tarif,
                    "avg_total_tarif": avg_total_tarif,
                }, status=status.HTTP_200_OK)
        elif jenis_mekanisme == 'mekanisme_langganan_umum':
            min_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.intensitas * ketentuan_mekanisme.min_tarif_dasar
            max_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.intensitas * ketentuan_mekanisme.max_tarif_dasar
            avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

            return Response({
                "jenis_mekanisme": jenis_mekanisme,
                "min_total_tarif": min_total_tarif,
                "max_total_tarif": max_total_tarif,
                "avg_total_tarif": avg_total_tarif,
            }, status=status.HTTP_200_OK)

        elif jenis_mekanisme == 'mekanisme_langganan_khusus':
            min_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.kali_parkir * ketentuan_mekanisme.min_tarif_dasar * ketentuan_mekanisme.multiplier
            max_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.kali_parkir * ketentuan_mekanisme.max_tarif_dasar * ketentuan_mekanisme.multiplier
            avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

            return Response({
                "jenis_mekanisme": jenis_mekanisme,
                "min_total_tarif": min_total_tarif,
                "max_total_tarif": max_total_tarif,
                "avg_total_tarif": avg_total_tarif,
            }, status=status.HTTP_200_OK)


class HitungTarifGedung(APIView):

    def get(self, request):
        jenis = request.query_params.get('jenis', '')
        jam = request.query_params.get('jam', '')
        kendaraan = request.query_params.get('kendaraan', '')

        if not (jenis and jam and kendaraan):
            return Response({
                "error": "Query parameter is missing"
            }, status=status.HTTP_400_BAD_REQUEST)

        if jenis not in ['harian', 'langganan_umum', 'langganan_khusus']:
            return Response({
                "error": "Jenis is wrong (Option: harian | langganan_umum | langganan_khusus)"
            }, status=status.HTTP_400_BAD_REQUEST)

        if not jam.isdigit() or int(jam) < 0:
            return Response({
                "error": "Jam is not valid"
            }, status=status.HTTP_400_BAD_REQUEST)

        if kendaraan not in ['sedan', 'jeep', 'minibus', 'pickup', 'bus', 'truk', 'sepeda motor', 'sepeda']:
            return Response({
                "error": "Kendaraan is wrong (Option: sedan | jeep | minibus | pickup | bus | truk | sepeda motor | sepeda)"
            }, status=status.HTTP_400_BAD_REQUEST)

        jam = int(jam)

        tipe_mekanisme = {
            "harian": "mekanisme_harian",
            "langganan_umum": "mekanisme_langganan_umum",
            "langganan_khusus": "mekanisme_langganan_khusus"
        }

        mekanisme = MekanismeTarifGedung.objects.get(jenis_kendaraan__nama=kendaraan)
        jenis_mekanisme = tipe_mekanisme[jenis]
        ketentuan_mekanisme = getattr(mekanisme, jenis_mekanisme)

        if jenis_mekanisme == 'mekanisme_harian':
            if ketentuan_mekanisme.cara_pembayaran == 'per jam':
                sisa_jam = 0 if (jam - 1) < 0 else jam - 1
                min_total_tarif = ketentuan_mekanisme.min_tarif_jam_pertama + ketentuan_mekanisme.min_tarif_jam_berikutnya * sisa_jam
                max_total_tarif = ketentuan_mekanisme.max_tarif_jam_pertama + ketentuan_mekanisme.max_tarif_jam_berikutnya * sisa_jam
                avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

                return Response({
                    "cara_pembayaran": ketentuan_mekanisme.cara_pembayaran,
                    "min_total_tarif": min_total_tarif,
                    "max_total_tarif": max_total_tarif,
                    "avg_total_tarif": avg_total_tarif,
                }, status=status.HTTP_200_OK)
            elif ketentuan_mekanisme.cara_pembayaran == 'satu kali parkir':
                min_total_tarif = ketentuan_mekanisme.min_tarif_jam_pertama
                max_total_tarif = ketentuan_mekanisme.max_tarif_jam_pertama
                avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

                return Response({
                    "cara_pembayaran": ketentuan_mekanisme.cara_pembayaran,
                    "min_total_tarif": min_total_tarif,
                    "max_total_tarif": max_total_tarif,
                    "avg_total_tarif": avg_total_tarif,
                }, status=status.HTTP_200_OK)
        elif jenis_mekanisme == 'mekanisme_langganan_umum':
            min_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.intensitas * ketentuan_mekanisme.min_tarif_dasar
            max_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.intensitas * ketentuan_mekanisme.max_tarif_dasar
            avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

            return Response({
                "jenis_mekanisme": jenis_mekanisme,
                "min_total_tarif": min_total_tarif,
                "max_total_tarif": max_total_tarif,
                "avg_total_tarif": avg_total_tarif,
            }, status=status.HTTP_200_OK)

        elif jenis_mekanisme == 'mekanisme_langganan_khusus':
            min_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.kali_parkir * ketentuan_mekanisme.min_tarif_dasar * ketentuan_mekanisme.multiplier
            max_total_tarif = ketentuan_mekanisme.hari * ketentuan_mekanisme.kali_parkir * ketentuan_mekanisme.max_tarif_dasar * ketentuan_mekanisme.multiplier
            avg_total_tarif = (min_total_tarif + max_total_tarif) / 2

            return Response({
                "jenis_mekanisme": jenis_mekanisme,
                "min_total_tarif": min_total_tarif,
                "max_total_tarif": max_total_tarif,
                "avg_total_tarif": avg_total_tarif,
            }, status=status.HTTP_200_OK)


class HitungTarifPenitipan(APIView):
    def get(self, request):
        hari = request.query_params.get('hari', '')
        kendaraan = request.query_params.get('kendaraan', '')

        print(hari)
        print(kendaraan)

        if not (hari and kendaraan):
            return Response({
                "error": "Query parameter is missing"
            }, status=status.HTTP_400_BAD_REQUEST)

        if kendaraan not in ['sedan', 'jeep', 'minibus', 'pickup', 'bus', 'truk', 'sepeda motor', 'sepeda']:
            return Response({
                "error": "Kendaraan is wrong (Option: sedan | jeep | minibus | pickup | bus | truk | sepeda motor | sepeda)"
            }, status=status.HTTP_400_BAD_REQUEST)

        if not hari:
            return Response({
                "error": "Query parameter is missing"
            }, status=status.HTTP_400_BAD_REQUEST)

        if not hari.isdigit() or int(hari) < 0:
            return Response({
                "error": "Hari is not valid"
            }, status=status.HTTP_400_BAD_REQUEST)

        hari = int(hari)

        mekanisme = MekanismeTarifPenitipanKendaraan.objects.get(jenis_kendaraan__nama=kendaraan)

        return Response({
            "jenis_mekanisme": mekanisme.cara_pembayaran,
            "total_tarif": mekanisme.tarif * hari,
        }, status=status.HTTP_200_OK)
