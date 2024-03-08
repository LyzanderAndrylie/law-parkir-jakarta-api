JENIS_PARKIR = [
    ('ruang milik jalan', 'ruang milik jalan'),
    ('lingkungan', 'lingkungan'),
    ('pelataran', 'pelataran'),
    ('gedung', 'gedung'),
    ('park and ride', 'park and ride'),
    ('vallet', 'vallet'),
    ('terminal parkir elektronik', 'terminal parkir elektronik'),
]

JENIS_GOLONGAN_RUMIJA = [
    ('jalan kawasan pengendalian parkir (KPP)', 'jalan kawasan pengendalian parkir (KPP)'),
    ('jalan A', 'jalan A'),
    ('jalan B', 'jalan B'),
]

JENIS_KENDARAAN = [
    ('sedan', 'sedan'),
    ('jeep', 'jeep'),
    ('minibus', 'minibus'),
    ('pickup', 'pickup'),
    ('bus', 'bus'),
    ('truk', 'truk'),
    ('sepeda motor', 'sepeda motor'),
    ('sepeda', 'sepeda'),
]

CARA_PEMBAYARAN = [
    ('per jam', 'per jam'),
    ('satu kali parkir', 'satu kali parkir'),
    ('per hari', 'per hari'),
]

JENIS_PENGGUNAAN_LAHAN = [
    ('menetap', 'menetap'),
    ('tidak menetap', 'tidak menetap'),
]

MEKANISME_URL_MAPPING = {
    "ruang milik jalan": 'mekanisme-rumija',
    'lingkungan': 'mekanisme-lingkungan',
    'pelataran': 'mekanisme-pelataran',
    'gedung': 'mekanisme-gedung',
    'penitipan kendaraan': 'mekanisme-penitipan',
    'park and ride': 'mekanisme-park-and-ride',
    'vallet': 'mekanisme-vallet',
    'terminal parkir elektronik': 'mekanisme-tpe'
}
