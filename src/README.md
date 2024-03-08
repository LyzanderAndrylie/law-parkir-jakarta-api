# Panduan cara menjalankan Django Project pada Local Development Environment

Pastikan bahwa `Python`, `pip`, dan `postgresql` sudah ter-*install* pada komputer kalian.

1. Clone repository

    ```shell
    git clone https://github.com/LyzanderAndrylie/law-parkir-jakarta-api
    ```

2. Buat virtual environment

    ```shell
    python -m venv env
    ```

3. Aktifkan virtual environment

    ```shell
    env\Scripts\activate
    ```

    > Note: Perintah di atas dijalankan pada sistem operasi Windows

4. Install semua *dependencies*

    ```shell
    pip install -r requirements.txt
    ```

5. Masukkan `.env` file pada folder project `parkir_api`.

    `DB_USER` dan `DB_PASSWORD` dapat Anda sesuaikan dengan `username` dan `password` akun postgres Anda.

    > :memo: Note: Perhatikan bahwa pada **production enviroment** `SECRET_KEY` harus di-*generate* [^1] dan `DEBUG` di-*set* dengan `False`.

6. Buat database `parkir_api` pada `postgresql`.

    ```postgresql
    CREATE DATABASE parkir_api;
    ```

7. Jalankan migrasi

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

8. Jalankan seeding database

    ```shell
    python manage.py loaddata lokasi-parkir jenis-tarif mekanisme-tarif kendaraan mekanisme-rumija mekanisme-lingkungan mekanisme-pelataran mekanisme-gedung mekanisme-penitipan mekanisme-park-and-ride mekanisme-vallet mekanisme-tpe jenis-langganan-tpe tarif-langganan-tpe
    ```

9. Jalankan development server

    ```shell
    python manage.py runserver
    ```

[^1]: [How to Generate a Secret Key in Django](https://codinggear.blog/django-generate-secret-key/#:~:text=Secret%20Key%20Safe-,What%20is%20a%20Django%20secret%20key%3F,of%20our%20hashes%20and%20tokens.)