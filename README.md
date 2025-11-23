# TUGAS-PRAKTIKUM-5-PERTEMUAN-10.
# Nama : Iyam Maryam <br>
# Nim  : 312510498 <br>
# Kelas: TI.25.C5 <br>

# Program Manajemen Nilai Mahasiswa

Program ini adalah aplikasi sederhana berbasis konsol untuk mengelola data nilai mahasiswa menggunakan struktur data `Dictionary` di Python.

## Fitur

Program ini menyediakan beberapa fitur utama untuk manajemen data nilai mahasiswa:

1.  **Tambah Data**: Memungkinkan pengguna untuk memasukkan data mahasiswa baru, termasuk nama, NIM, dan nilai untuk tugas, UTS, serta UAS.
2.  **Ubah Data**: Memungkinkan pengguna untuk mengubah data nilai yang sudah ada untuk mahasiswa tertentu.
3.  **Hapus Data**: Memungkinkan pengguna untuk menghapus data mahasiswa dari sistem.
4.  **Tampilkan Data**: Menampilkan daftar lengkap semua mahasiswa beserta nilai-nilai dan nilai akhir mereka.
5.  **Cari Data**: Memungkinkan pengguna untuk mencari data mahasiswa berdasarkan nama atau NIM.

## Perhitungan Nilai Akhir

Nilai akhir mahasiswa dihitung berdasarkan 3 komponen nilai dengan bobot sebagai berikut:

* **Tugas**: 30%
* **UTS (Ujian Tengah Semester)**: 35%
* **UAS (Ujian Akhir Semester)**: 35%

Rumus perhitungan: `Nilai Akhir = (Tugas * 0.30) + (UTS * 0.35) + (UAS * 0.35)`

## Flowchart Program

Berikut adalah representasi visual dari alur kerja program:

```mermaid
graph TD
    A[Start] --> B{Pilih Opsi};
    B -- "Tambah Data" --> C[Input Data Mahasiswa dan Nilai];
    C --> D[Hitung Nilai Akhir];
    D --> E[Simpan Data ke Dictionary];
    E --> B;

    B -- "Ubah Data" --> F[Pilih Mahasiswa untuk Diubah];
    F --> G[Update Data Mahasiswa/Nilai];
    G --> D;

    B -- "Hapus Data" --> H[Pilih Mahasiswa untuk Dihapus];
    H --> I[Hapus Data dari Dictionary];
    I --> B;

    B -- "Tampilkan Data" --> J[Tampilkan Semua Data Mahasiswa];
    J --> B;

    B -- "Cari Data" --> K[Masukkan Nama/NIM Mahasiswa];
    K --> L{Data Ditemukan?};
    L -- "Ya" --> M[Tampilkan Detail Mahasiswa];
    L -- "Tidak" --> N[Pesan: Data Tidak Ditemukan];
    M --> B;
    N --> B;

    B -- "Exit" --> O[End];

![alt image]()
