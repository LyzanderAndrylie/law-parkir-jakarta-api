# LAW - Parkir Jakarta API
# 📁 Folder: Lokasi Parkir 


## End-point: Daftar Lokasi Parkir
### Method: GET
>```
>/api/v1/lokasi
>```
### Response: 200
```json
{
    "count": 45,
    "next": "http://localhost:8000/api/v1/lokasi/?page=2",
    "previous": null,
    "results": [
        {
            "periode_data": "2018",
            "nama": "Gedung Parkir Istana Pasar Baru  8 Lt",
            "jenis": "gedung",
            "alamat": "Jln  Pintu Air Raya",
            "luas_m2": 12432,
            "kapasitas_mobil": 445,
            "kapasitas_motor": 130,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/1/"
        },
        {
            "periode_data": "2018",
            "nama": "Gedung Parkir Taman Menteng  3 Lt",
            "jenis": "gedung",
            "alamat": "Jln  HOS Cokroaminoto No  9 Jakarta Pusat",
            "luas_m2": 4455,
            "kapasitas_mobil": 152,
            "kapasitas_motor": 300,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/2/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Parkir IRTI Monas",
            "jenis": "pelataran",
            "alamat": "Jln  Medan Merdeka Selatan",
            "luas_m2": 18450,
            "kapasitas_mobil": 352,
            "kapasitas_motor": 1250,
            "kapasitas_bus_truk": 12,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/3/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Ex Gedung Parkir Glodok",
            "jenis": "pelataran",
            "alamat": "Jln  Pintu Besar Selatan No  1",
            "luas_m2": 4640,
            "kapasitas_mobil": 80,
            "kapasitas_motor": 180,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/4/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Cengkeh Taman Kota Intan",
            "jenis": "pelataran",
            "alamat": "Jln  Cengkeh",
            "luas_m2": 3408,
            "kapasitas_mobil": 85,
            "kapasitas_motor": 120,
            "kapasitas_bus_truk": 12,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/5/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Taman Ismail Marzuki  TIM",
            "jenis": "pelataran",
            "alamat": "Jln  Cikini Raya",
            "luas_m2": 3801,
            "kapasitas_mobil": 240,
            "kapasitas_motor": 470,
            "kapasitas_bus_truk": 8,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/6/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Thamrin 10",
            "jenis": "pelataran",
            "alamat": "Jln  MH Thamrin No 10",
            "luas_m2": 2720,
            "kapasitas_mobil": 250,
            "kapasitas_motor": 0,
            "kapasitas_bus_truk": 15,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/7/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Parkir Pulogebang",
            "jenis": "pelataran",
            "alamat": "Terminal Terpadu Pulogebang",
            "luas_m2": 962,
            "kapasitas_mobil": 170,
            "kapasitas_motor": 250,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/8/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Parkir Unit PKB dan BBN KB Jakarta Pusat dan Utara",
            "jenis": "pelataran",
            "alamat": "Jln  Gunung Sahari No  13",
            "luas_m2": 3804,
            "kapasitas_mobil": 180,
            "kapasitas_motor": 800,
            "kapasitas_bus_truk": 6,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/9/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Parkir Unit PKB dan BBN KB Jakarta Timur",
            "jenis": "pelataran",
            "alamat": "Jln  D I Panjaitan Kav  55",
            "luas_m2": 7292,
            "kapasitas_mobil": 400,
            "kapasitas_motor": 1097,
            "kapasitas_bus_truk": 11,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/10/"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Lokasi Parkir
### Method: GET
>```
>/api/v1/lokasi/1
>```
### Response: 200
```json
{
    "periode_data": "2018",
    "nama": "Gedung Parkir Istana Pasar Baru  8 Lt",
    "jenis": "gedung",
    "alamat": "Jln  Pintu Air Raya",
    "luas_m2": 12432,
    "kapasitas_mobil": 445,
    "kapasitas_motor": 130,
    "kapasitas_bus_truk": 0,
    "daftar_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Cari Lokasi Parkir
### Method: GET
>```
>/api/v1/lokasi?search=pasar baru&jenis=gedung
>```
### Query Params

|Param|value|
|---|---|
|search|pasar baru|
|jenis|gedung|
|kapasitas_mobil|352|
|kapasitas_motor|1250|
|kapasitas_bus_truk|12|
|min_luas_m2|5000|
|max_luas_m2|5000|
|max_kapasitas_mobil|50|
|min_kapasitas_mobil|50|
|max_kapasitas_motor|1250|
|min_kapasitas_motor|1250|
|max_kapasitas_bus_truk|5|
|min_kapasitas_bus_truk|5|


### Response: 200
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "periode_data": "2018",
            "nama": "Gedung Parkir Istana Pasar Baru  8 Lt",
            "jenis": "gedung",
            "alamat": "Jln  Pintu Air Raya",
            "luas_m2": 12432,
            "kapasitas_mobil": 445,
            "kapasitas_motor": 130,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/1/"
        },
        {
            "periode_data": "2019",
            "nama": "Gedung Parkir Istana Pasar Baru  8 Lt",
            "jenis": "gedung",
            "alamat": "Jln  Pintu Air Raya",
            "luas_m2": 12432,
            "kapasitas_mobil": 445,
            "kapasitas_motor": 130,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/16/"
        },
        {
            "periode_data": "2017",
            "nama": "Gedung Parkir Istana Pasar Baru  8 Lt",
            "jenis": "gedung",
            "alamat": "Jln  Pintu Air Raya",
            "luas_m2": 12432,
            "kapasitas_mobil": 445,
            "kapasitas_motor": 130,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/31/"
        }
    ]
}
```

### Response: 200
```json
{
    "count": 30,
    "next": "http://localhost:8000/api/v1/lokasi/?jenis=pelataran&page=2",
    "previous": null,
    "results": [
        {
            "periode_data": "2018",
            "nama": "Pelataran Parkir IRTI Monas",
            "jenis": "pelataran",
            "alamat": "Jln  Medan Merdeka Selatan",
            "luas_m2": 18450,
            "kapasitas_mobil": 352,
            "kapasitas_motor": 1250,
            "kapasitas_bus_truk": 12,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/3/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Ex Gedung Parkir Glodok",
            "jenis": "pelataran",
            "alamat": "Jln  Pintu Besar Selatan No  1",
            "luas_m2": 4640,
            "kapasitas_mobil": 80,
            "kapasitas_motor": 180,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/4/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Cengkeh Taman Kota Intan",
            "jenis": "pelataran",
            "alamat": "Jln  Cengkeh",
            "luas_m2": 3408,
            "kapasitas_mobil": 85,
            "kapasitas_motor": 120,
            "kapasitas_bus_truk": 12,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/5/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Taman Ismail Marzuki  TIM",
            "jenis": "pelataran",
            "alamat": "Jln  Cikini Raya",
            "luas_m2": 3801,
            "kapasitas_mobil": 240,
            "kapasitas_motor": 470,
            "kapasitas_bus_truk": 8,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/6/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Thamrin 10",
            "jenis": "pelataran",
            "alamat": "Jln  MH Thamrin No 10",
            "luas_m2": 2720,
            "kapasitas_mobil": 250,
            "kapasitas_motor": 0,
            "kapasitas_bus_truk": 15,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/7/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Parkir Pulogebang",
            "jenis": "pelataran",
            "alamat": "Terminal Terpadu Pulogebang",
            "luas_m2": 962,
            "kapasitas_mobil": 170,
            "kapasitas_motor": 250,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/8/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Parkir Unit PKB dan BBN KB Jakarta Pusat dan Utara",
            "jenis": "pelataran",
            "alamat": "Jln  Gunung Sahari No  13",
            "luas_m2": 3804,
            "kapasitas_mobil": 180,
            "kapasitas_motor": 800,
            "kapasitas_bus_truk": 6,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/9/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Parkir Unit PKB dan BBN KB Jakarta Timur",
            "jenis": "pelataran",
            "alamat": "Jln  D I Panjaitan Kav  55",
            "luas_m2": 7292,
            "kapasitas_mobil": 400,
            "kapasitas_motor": 1097,
            "kapasitas_bus_truk": 11,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/10/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Parkir Unit PKB dan BBN KB Jakarta Barat",
            "jenis": "pelataran",
            "alamat": "Jln  Daan Mogot KM 13",
            "luas_m2": 3443,
            "kapasitas_mobil": 120,
            "kapasitas_motor": 720,
            "kapasitas_bus_truk": 4,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/11/"
        },
        {
            "periode_data": "2018",
            "nama": "Pelataran Parkir RPTRA Kalijodo",
            "jenis": "pelataran",
            "alamat": "Jln  Pangeran Tubagus Angke No 19",
            "luas_m2": 13632,
            "kapasitas_mobil": 113,
            "kapasitas_motor": 1200,
            "kapasitas_bus_truk": 10,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/12/"
        }
    ]
}
```

### Response: 200
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "periode_data": "2018",
            "nama": "Gedung Parkir Istana Pasar Baru  8 Lt",
            "jenis": "gedung",
            "alamat": "Jln  Pintu Air Raya",
            "luas_m2": 12432,
            "kapasitas_mobil": 445,
            "kapasitas_motor": 130,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/1/"
        },
        {
            "periode_data": "2019",
            "nama": "Gedung Parkir Istana Pasar Baru  8 Lt",
            "jenis": "gedung",
            "alamat": "Jln  Pintu Air Raya",
            "luas_m2": 12432,
            "kapasitas_mobil": 445,
            "kapasitas_motor": 130,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/16/"
        },
        {
            "periode_data": "2017",
            "nama": "Gedung Parkir Istana Pasar Baru  8 Lt",
            "jenis": "gedung",
            "alamat": "Jln  Pintu Air Raya",
            "luas_m2": 12432,
            "kapasitas_mobil": 445,
            "kapasitas_motor": 130,
            "kapasitas_bus_truk": 0,
            "detail_lokasi_parkir": "http://localhost:8000/api/v1/lokasi/31/"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Tarif Parkir 


## End-point: Rumija
### Method: GET
>```
>/api/v1/mekanisme-rumija/
>```
### Response: 200
```json
{
    "count": 12,
    "next": "http://localhost:8000/api/v1/mekanisme-rumija/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "golongan": "jalan kawasan pengendalian parkir (KPP)",
            "min_tarif": 3000,
            "max_tarif": 12000,
            "cara_pembayaran": "per jam",
            "jenis_tarif": 1,
            "jenis_kendaraan": [
                "sedan",
                "jeep",
                "minibus",
                "pickup"
            ]
        },
        {
            "id": 2,
            "golongan": "jalan kawasan pengendalian parkir (KPP)",
            "min_tarif": 4000,
            "max_tarif": 12000,
            "cara_pembayaran": "per jam",
            "jenis_tarif": 1,
            "jenis_kendaraan": [
                "bus",
                "truk"
            ]
        },
        {
            "id": 3,
            "golongan": "jalan kawasan pengendalian parkir (KPP)",
            "min_tarif": 2000,
            "max_tarif": 6000,
            "cara_pembayaran": "per jam",
            "jenis_tarif": 1,
            "jenis_kendaraan": [
                "sepeda motor"
            ]
        },
        {
            "id": 4,
            "golongan": "jalan kawasan pengendalian parkir (KPP)",
            "min_tarif": 1000,
            "max_tarif": 1000,
            "cara_pembayaran": "satu kali parkir",
            "jenis_tarif": 1,
            "jenis_kendaraan": [
                "sepeda"
            ]
        },
        {
            "id": 5,
            "golongan": "jalan A",
            "min_tarif": 3000,
            "max_tarif": 9000,
            "cara_pembayaran": "per jam",
            "jenis_tarif": 1,
            "jenis_kendaraan": [
                "sedan",
                "jeep",
                "minibus",
                "pickup"
            ]
        },
        {
            "id": 6,
            "golongan": "jalan A",
            "min_tarif": 4000,
            "max_tarif": 9000,
            "cara_pembayaran": "per jam",
            "jenis_tarif": 1,
            "jenis_kendaraan": [
                "bus",
                "truk"
            ]
        },
        {
            "id": 7,
            "golongan": "jalan A",
            "min_tarif": 2000,
            "max_tarif": 4500,
            "cara_pembayaran": "per jam",
            "jenis_tarif": 1,
            "jenis_kendaraan": [
                "sepeda motor"
            ]
        },
        {
            "id": 8,
            "golongan": "jalan A",
            "min_tarif": 1000,
            "max_tarif": 1000,
            "cara_pembayaran": "satu kali parkir",
            "jenis_tarif": 1,
            "jenis_kendaraan": [
                "sepeda"
            ]
        },
        {
            "id": 9,
            "golongan": "jalan B",
            "min_tarif": 2000,
            "max_tarif": 6000,
            "cara_pembayaran": "per jam",
            "jenis_tarif": 1,
            "jenis_kendaraan": [
                "sedan",
                "jeep",
                "minibus",
                "pickup"
            ]
        },
        {
            "id": 10,
            "golongan": "jalan B",
            "min_tarif": 4000,
            "max_tarif": 6000,
            "cara_pembayaran": "per jam",
            "jenis_tarif": 1,
            "jenis_kendaraan": [
                "bus",
                "truk"
            ]
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Lingkungan
### Method: GET
>```
>/api/v1/mekanisme-lingkungan/
>```
### Response: 200
```json
{
    "count": 12,
    "next": "http://localhost:8000/api/v1/mekanisme-lingkungan/?page=2",
    "previous": null,
    "results": [
        {
            "id": 13,
            "mekanisme_harian": {
                "id": 1,
                "min_tarif_jam_pertama": 4000,
                "max_tarif_jam_pertama": 7500,
                "min_tarif_jam_berikutnya": 2000,
                "max_tarif_jam_berikutnya": 6000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 1,
                "hari": 25,
                "intensitas": 3,
                "min_tarif_dasar": 4000,
                "max_tarif_dasar": 7500
            },
            "mekanisme_langganan_khusus": {
                "id": 1,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 4000,
                "max_tarif_dasar": 7500,
                "multiplier": 0.75
            },
            "jenis_kendaraan": [
                "sedan",
                "jeep",
                "minibus",
                "pickup"
            ]
        },
        {
            "id": 14,
            "mekanisme_harian": {
                "id": 2,
                "min_tarif_jam_pertama": 6000,
                "max_tarif_jam_pertama": 7000,
                "min_tarif_jam_berikutnya": 3000,
                "max_tarif_jam_berikutnya": 3000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 2,
                "hari": 25,
                "intensitas": 3,
                "min_tarif_dasar": 6000,
                "max_tarif_dasar": 7000
            },
            "mekanisme_langganan_khusus": {
                "id": 2,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 6000,
                "max_tarif_dasar": 7000,
                "multiplier": 0.75
            },
            "jenis_kendaraan": [
                "bus",
                "truk"
            ]
        },
        {
            "id": 15,
            "mekanisme_harian": {
                "id": 3,
                "min_tarif_jam_pertama": 1000,
                "max_tarif_jam_pertama": 3000,
                "min_tarif_jam_berikutnya": 1000,
                "max_tarif_jam_berikutnya": 3000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 3,
                "hari": 25,
                "intensitas": 2,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 3000
            },
            "mekanisme_langganan_khusus": {
                "id": 3,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 3000,
                "multiplier": 1
            },
            "jenis_kendaraan": [
                "sepeda motor"
            ]
        },
        {
            "id": 16,
            "mekanisme_harian": {
                "id": 4,
                "min_tarif_jam_pertama": 1000,
                "max_tarif_jam_pertama": 1000,
                "min_tarif_jam_berikutnya": 1000,
                "max_tarif_jam_berikutnya": 1000,
                "cara_pembayaran": "satu kali parkir"
            },
            "mekanisme_langganan_umum": {
                "id": 4,
                "hari": 25,
                "intensitas": 2,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 1000
            },
            "mekanisme_langganan_khusus": {
                "id": 4,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 1000,
                "multiplier": 1
            },
            "jenis_kendaraan": [
                "sepeda"
            ]
        },
        {
            "id": 17,
            "mekanisme_harian": {
                "id": 5,
                "min_tarif_jam_pertama": 4000,
                "max_tarif_jam_pertama": 7500,
                "min_tarif_jam_berikutnya": 2000,
                "max_tarif_jam_berikutnya": 6000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 5,
                "hari": 25,
                "intensitas": 3,
                "min_tarif_dasar": 4000,
                "max_tarif_dasar": 7500
            },
            "mekanisme_langganan_khusus": {
                "id": 5,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 4000,
                "max_tarif_dasar": 7500,
                "multiplier": 0.75
            },
            "jenis_kendaraan": [
                "sedan",
                "jeep",
                "minibus",
                "pickup"
            ]
        },
        {
            "id": 18,
            "mekanisme_harian": {
                "id": 6,
                "min_tarif_jam_pertama": 6000,
                "max_tarif_jam_pertama": 7000,
                "min_tarif_jam_berikutnya": 3000,
                "max_tarif_jam_berikutnya": 3000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 6,
                "hari": 25,
                "intensitas": 3,
                "min_tarif_dasar": 6000,
                "max_tarif_dasar": 7000
            },
            "mekanisme_langganan_khusus": {
                "id": 6,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 6000,
                "max_tarif_dasar": 7000,
                "multiplier": 0.75
            },
            "jenis_kendaraan": [
                "bus",
                "truk"
            ]
        },
        {
            "id": 19,
            "mekanisme_harian": {
                "id": 7,
                "min_tarif_jam_pertama": 1000,
                "max_tarif_jam_pertama": 3000,
                "min_tarif_jam_berikutnya": 1000,
                "max_tarif_jam_berikutnya": 3000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 7,
                "hari": 25,
                "intensitas": 2,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 3000
            },
            "mekanisme_langganan_khusus": {
                "id": 7,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 3000,
                "multiplier": 1
            },
            "jenis_kendaraan": [
                "sepeda motor"
            ]
        },
        {
            "id": 20,
            "mekanisme_harian": {
                "id": 8,
                "min_tarif_jam_pertama": 1000,
                "max_tarif_jam_pertama": 1000,
                "min_tarif_jam_berikutnya": 1000,
                "max_tarif_jam_berikutnya": 1000,
                "cara_pembayaran": "satu kali parkir"
            },
            "mekanisme_langganan_umum": {
                "id": 8,
                "hari": 25,
                "intensitas": 2,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 1000
            },
            "mekanisme_langganan_khusus": {
                "id": 8,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 1000,
                "multiplier": 1
            },
            "jenis_kendaraan": [
                "sepeda"
            ]
        },
        {
            "id": 21,
            "mekanisme_harian": {
                "id": 9,
                "min_tarif_jam_pertama": 4000,
                "max_tarif_jam_pertama": 10000,
                "min_tarif_jam_berikutnya": 2000,
                "max_tarif_jam_berikutnya": 8000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 9,
                "hari": 25,
                "intensitas": 3,
                "min_tarif_dasar": 4000,
                "max_tarif_dasar": 10000
            },
            "mekanisme_langganan_khusus": {
                "id": 9,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 4000,
                "max_tarif_dasar": 10000,
                "multiplier": 0.75
            },
            "jenis_kendaraan": [
                "sedan",
                "jeep",
                "minibus",
                "pickup"
            ]
        },
        {
            "id": 22,
            "mekanisme_harian": {
                "id": 10,
                "min_tarif_jam_pertama": 6000,
                "max_tarif_jam_pertama": 7000,
                "min_tarif_jam_berikutnya": 3000,
                "max_tarif_jam_berikutnya": 3000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 10,
                "hari": 25,
                "intensitas": 3,
                "min_tarif_dasar": 6000,
                "max_tarif_dasar": 7000
            },
            "mekanisme_langganan_khusus": {
                "id": 10,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 6000,
                "max_tarif_dasar": 7000,
                "multiplier": 0.75
            },
            "jenis_kendaraan": [
                "bus",
                "truk"
            ]
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Pelataran
### Method: GET
>```
>/api/v1/mekanisme-pelataran/
>```
### Response: 200
```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 17,
            "mekanisme_harian": {
                "id": 5,
                "min_tarif_jam_pertama": 4000,
                "max_tarif_jam_pertama": 7500,
                "min_tarif_jam_berikutnya": 2000,
                "max_tarif_jam_berikutnya": 6000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 5,
                "hari": 25,
                "intensitas": 3,
                "min_tarif_dasar": 4000,
                "max_tarif_dasar": 7500
            },
            "mekanisme_langganan_khusus": {
                "id": 5,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 4000,
                "max_tarif_dasar": 7500,
                "multiplier": 0.75
            },
            "jenis_kendaraan": [
                "sedan",
                "jeep",
                "minibus",
                "pickup"
            ]
        },
        {
            "id": 18,
            "mekanisme_harian": {
                "id": 6,
                "min_tarif_jam_pertama": 6000,
                "max_tarif_jam_pertama": 7000,
                "min_tarif_jam_berikutnya": 3000,
                "max_tarif_jam_berikutnya": 3000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 6,
                "hari": 25,
                "intensitas": 3,
                "min_tarif_dasar": 6000,
                "max_tarif_dasar": 7000
            },
            "mekanisme_langganan_khusus": {
                "id": 6,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 6000,
                "max_tarif_dasar": 7000,
                "multiplier": 0.75
            },
            "jenis_kendaraan": [
                "bus",
                "truk"
            ]
        },
        {
            "id": 19,
            "mekanisme_harian": {
                "id": 7,
                "min_tarif_jam_pertama": 1000,
                "max_tarif_jam_pertama": 3000,
                "min_tarif_jam_berikutnya": 1000,
                "max_tarif_jam_berikutnya": 3000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 7,
                "hari": 25,
                "intensitas": 2,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 3000
            },
            "mekanisme_langganan_khusus": {
                "id": 7,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 3000,
                "multiplier": 1
            },
            "jenis_kendaraan": [
                "sepeda motor"
            ]
        },
        {
            "id": 20,
            "mekanisme_harian": {
                "id": 8,
                "min_tarif_jam_pertama": 1000,
                "max_tarif_jam_pertama": 1000,
                "min_tarif_jam_berikutnya": 1000,
                "max_tarif_jam_berikutnya": 1000,
                "cara_pembayaran": "satu kali parkir"
            },
            "mekanisme_langganan_umum": {
                "id": 8,
                "hari": 25,
                "intensitas": 2,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 1000
            },
            "mekanisme_langganan_khusus": {
                "id": 8,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 1000,
                "multiplier": 1
            },
            "jenis_kendaraan": [
                "sepeda"
            ]
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Gedung
### Method: GET
>```
>/api/v1/mekanisme-gedung/
>```
### Response: 200
```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 21,
            "mekanisme_harian": {
                "id": 9,
                "min_tarif_jam_pertama": 4000,
                "max_tarif_jam_pertama": 10000,
                "min_tarif_jam_berikutnya": 2000,
                "max_tarif_jam_berikutnya": 8000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 9,
                "hari": 25,
                "intensitas": 3,
                "min_tarif_dasar": 4000,
                "max_tarif_dasar": 10000
            },
            "mekanisme_langganan_khusus": {
                "id": 9,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 4000,
                "max_tarif_dasar": 10000,
                "multiplier": 0.75
            },
            "jenis_kendaraan": [
                "sedan",
                "jeep",
                "minibus",
                "pickup"
            ]
        },
        {
            "id": 22,
            "mekanisme_harian": {
                "id": 10,
                "min_tarif_jam_pertama": 6000,
                "max_tarif_jam_pertama": 7000,
                "min_tarif_jam_berikutnya": 3000,
                "max_tarif_jam_berikutnya": 3000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 10,
                "hari": 25,
                "intensitas": 3,
                "min_tarif_dasar": 6000,
                "max_tarif_dasar": 7000
            },
            "mekanisme_langganan_khusus": {
                "id": 10,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 6000,
                "max_tarif_dasar": 7000,
                "multiplier": 0.75
            },
            "jenis_kendaraan": [
                "bus",
                "truk"
            ]
        },
        {
            "id": 23,
            "mekanisme_harian": {
                "id": 11,
                "min_tarif_jam_pertama": 1000,
                "max_tarif_jam_pertama": 4000,
                "min_tarif_jam_berikutnya": 1000,
                "max_tarif_jam_berikutnya": 4000,
                "cara_pembayaran": "per jam"
            },
            "mekanisme_langganan_umum": {
                "id": 11,
                "hari": 25,
                "intensitas": 2,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 4000
            },
            "mekanisme_langganan_khusus": {
                "id": 11,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 4000,
                "multiplier": 1
            },
            "jenis_kendaraan": [
                "sepeda motor"
            ]
        },
        {
            "id": 24,
            "mekanisme_harian": {
                "id": 12,
                "min_tarif_jam_pertama": 1000,
                "max_tarif_jam_pertama": 1000,
                "min_tarif_jam_berikutnya": 1000,
                "max_tarif_jam_berikutnya": 1000,
                "cara_pembayaran": "satu kali parkir"
            },
            "mekanisme_langganan_umum": {
                "id": 12,
                "hari": 25,
                "intensitas": 2,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 1000
            },
            "mekanisme_langganan_khusus": {
                "id": 12,
                "hari": 22,
                "kali_parkir": 1,
                "min_tarif_dasar": 1000,
                "max_tarif_dasar": 1000,
                "multiplier": 1
            },
            "jenis_kendaraan": [
                "sepeda"
            ]
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Penitipan
### Method: GET
>```
>/api/v1/mekanisme-penitipan/
>```
### Response: 200
```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 25,
            "tarif": 45000,
            "cara_pembayaran": "per hari",
            "jenis_kendaraan": [
                "sedan",
                "jeep",
                "minibus",
                "pickup"
            ]
        },
        {
            "id": 26,
            "tarif": 85000,
            "cara_pembayaran": "per hari",
            "jenis_kendaraan": [
                "bus",
                "truk"
            ]
        },
        {
            "id": 27,
            "tarif": 25000,
            "cara_pembayaran": "per hari",
            "jenis_kendaraan": [
                "sepeda motor"
            ]
        },
        {
            "id": 28,
            "tarif": 10000,
            "cara_pembayaran": "per hari",
            "jenis_kendaraan": [
                "sepeda"
            ]
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Park and ride
### Method: GET
>```
>/api/v1/mekanisme-park-and-ride/
>```
### Response: 200
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 29,
            "tarif": 5000,
            "cara_pembayaran": "satu kali parkir",
            "jenis_kendaraan": [
                "sedan",
                "jeep",
                "minibus",
                "pickup",
                "bus",
                "truk"
            ]
        },
        {
            "id": 30,
            "tarif": 2000,
            "cara_pembayaran": "satu kali parkir",
            "jenis_kendaraan": [
                "sepeda motor"
            ]
        },
        {
            "id": 31,
            "tarif": 1000,
            "cara_pembayaran": "satu kali parkir",
            "jenis_kendaraan": [
                "sepeda"
            ]
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Vallet
### Method: GET
>```
>/api/v1/mekanisme-vallet/
>```
### Response: 200
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 32,
            "min_tarif": 20000,
            "max_tarif": 50000,
            "jenis_tarif": 7
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: TPE
### Method: GET
>```
>/api/v1/mekanisme-tpe/
>```
### Response: 200
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "tarif_harian": {
                "id": 1,
                "nama": "ruang milik jalan"
            },
            "tarif_langganan": [
                {
                    "id": 1,
                    "jenis_kendaraan": [
                        "sedan",
                        "jeep",
                        "minibus",
                        "pickup"
                    ],
                    "total_hari": 0,
                    "tarif_hari_jam": 5000,
                    "tarif_tpe": {
                        "id": 33,
                        "jenis_tarif": 8,
                        "tarif_harian": 1
                    },
                    "jenis_langganan_per_hari": [
                        {
                            "id": 1,
                            "jam": 12,
                            "jenis_penggunaan_lahan_parkir": "menetap"
                        },
                        {
                            "id": 2,
                            "jam": 4,
                            "jenis_penggunaan_lahan_parkir": "tidak menetap"
                        },
                        {
                            "id": 3,
                            "jam": 2,
                            "jenis_penggunaan_lahan_parkir": "tidak menetap"
                        }
                    ]
                },
                {
                    "id": 2,
                    "jenis_kendaraan": [
                        "bus",
                        "truk"
                    ],
                    "total_hari": 0,
                    "tarif_hari_jam": 8000,
                    "tarif_tpe": {
                        "id": 33,
                        "jenis_tarif": 8,
                        "tarif_harian": 1
                    },
                    "jenis_langganan_per_hari": [
                        {
                            "id": 1,
                            "jam": 12,
                            "jenis_penggunaan_lahan_parkir": "menetap"
                        },
                        {
                            "id": 2,
                            "jam": 4,
                            "jenis_penggunaan_lahan_parkir": "tidak menetap"
                        },
                        {
                            "id": 3,
                            "jam": 2,
                            "jenis_penggunaan_lahan_parkir": "tidak menetap"
                        }
                    ]
                },
                {
                    "id": 3,
                    "jenis_kendaraan": [
                        "sepeda motor"
                    ],
                    "total_hari": 0,
                    "tarif_hari_jam": 2000,
                    "tarif_tpe": {
                        "id": 33,
                        "jenis_tarif": 8,
                        "tarif_harian": 1
                    },
                    "jenis_langganan_per_hari": [
                        {
                            "id": 1,
                            "jam": 12,
                            "jenis_penggunaan_lahan_parkir": "menetap"
                        },
                        {
                            "id": 2,
                            "jam": 4,
                            "jenis_penggunaan_lahan_parkir": "tidak menetap"
                        },
                        {
                            "id": 3,
                            "jam": 2,
                            "jenis_penggunaan_lahan_parkir": "tidak menetap"
                        }
                    ]
                },
                {
                    "id": 4,
                    "jenis_kendaraan": [
                        "sepeda"
                    ],
                    "total_hari": 0,
                    "tarif_hari_jam": 1000,
                    "tarif_tpe": {
                        "id": 33,
                        "jenis_tarif": 8,
                        "tarif_harian": 1
                    },
                    "jenis_langganan_per_hari": [
                        {
                            "id": 1,
                            "jam": 12,
                            "jenis_penggunaan_lahan_parkir": "menetap"
                        },
                        {
                            "id": 2,
                            "jam": 4,
                            "jenis_penggunaan_lahan_parkir": "tidak menetap"
                        },
                        {
                            "id": 3,
                            "jam": 2,
                            "jenis_penggunaan_lahan_parkir": "tidak menetap"
                        }
                    ]
                }
            ]
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Daftar Jenis Layanan Parkir
### Method: GET
>```
>/api/v1/tarif/
>```
### Response: 200
```json
{
    "count": 8,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "ruang milik jalan",
            "daftar_mekanisme": "http://localhost:8000/mekanisme-rumija"
        },
        {
            "name": "lingkungan",
            "daftar_mekanisme": "http://localhost:8000/mekanisme-lingkungan"
        },
        {
            "name": "pelataran",
            "daftar_mekanisme": "http://localhost:8000/mekanisme-pelataran"
        },
        {
            "name": "gedung",
            "daftar_mekanisme": "http://localhost:8000/mekanisme-gedung"
        },
        {
            "name": "penitipan kendaraan",
            "daftar_mekanisme": "http://localhost:8000/mekanisme-penitipan"
        },
        {
            "name": "park and ride",
            "daftar_mekanisme": "http://localhost:8000/mekanisme-park-and-ride"
        },
        {
            "name": "vallet",
            "daftar_mekanisme": "http://localhost:8000/mekanisme-vallet"
        },
        {
            "name": "terminal parkir elektronik",
            "daftar_mekanisme": "http://localhost:8000/mekanisme-tpe"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Folder: Perhitungan Tarif 


## End-point: Rumija
### Method: GET
>```
>/api/v1/mekanisme-rumija/tarif?golongan=kpp&kendaraan=sedan&jam=10
>```
### Query Params

|Param|value|
|---|---|
|golongan|kpp|
|kendaraan|sedan|
|jam|10|


### Response: 200
```json
{
    "golongan": "jalan kawasan pengendalian parkir (KPP)",
    "cara_pembayaran": "per jam",
    "min_total_tarif": 30000,
    "max_total_tarif": 120000,
    "avg_total_tarif": 75000
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Lingkungan
### Method: GET
>```
>/api/v1/mekanisme-lingkungan/tarif?jenis=harian&kendaraan=jeep&jam=2
>```
### Query Params

|Param|value|
|---|---|
|jenis|harian|
|kendaraan|jeep|
|jam|2|


### Response: 200
```json
{
    "jenis_mekanisme": "mekanisme_langganan_umum",
    "min_total_tarif": 50000,
    "max_total_tarif": 150000,
    "avg_total_tarif": 100000
}
```

### Response: 200
```json
{
    "cara_pembayaran": "per jam",
    "min_total_tarif": 4000,
    "max_total_tarif": 7500,
    "avg_total_tarif": 5750
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Pelataran
### Method: GET
>```
>/api/v1/mekanisme-pelataran/tarif?jenis=harian&kendaraan=sepeda motor&jam=1
>```
### Query Params

|Param|value|
|---|---|
|jenis|harian|
|kendaraan|sepeda motor|
|jam|1|


### Response: 200
```json
{
    "cara_pembayaran": "per jam",
    "min_total_tarif": 10000,
    "max_total_tarif": 30000,
    "avg_total_tarif": 20000
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Gedung
### Method: GET
>```
>/api/v1/mekanisme-gedung/tarif?jenis=harian&kendaraan=pickup&jam=2
>```
### Query Params

|Param|value|
|---|---|
|jenis|harian|
|kendaraan|pickup|
|jam|2|


### Response: 200
```json
{
    "cara_pembayaran": "per jam",
    "min_total_tarif": 6000,
    "max_total_tarif": 18000,
    "avg_total_tarif": 12000
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Penitipan
### Method: GET
>```
>/api/v1/mekanisme-penitipan/tarif?hari=5&kendaraan=sepeda
>```
### Query Params

|Param|value|
|---|---|
|hari|5|
|kendaraan|sepeda|


### Response: 200
```json
{
    "jenis_mekanisme": "per hari",
    "total_tarif": 50000
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
