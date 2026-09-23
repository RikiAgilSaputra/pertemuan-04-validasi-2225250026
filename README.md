# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input
Nama: Riki Agil Saputra


NIM: 2225250026


Kelas: 3A


## Tujuan
Membangun program validasi dan klasifikasi dengan rantai if-elif-else.
## Cara Menjalankan
python3 praktik/validasi_klasifikasi_nilai.py
## Tabel Keputusan
| No. | Kategori/Cabang                 | Syarat/Kondisi                                          | Contoh Masukan (Ujian, Tugas, Kehadiran) | Keluaran                                                                     |
| --: | ------------------------------- | ------------------------------------------------------- | ---------------------------------------- | ---------------------------------------------------------------------------- |
|   1 | Input tidak valid – tipe data   | Salah satu input tidak dapat dikonversi menjadi `float` | `80, 75, abc`                            | Masukkan ditolak: seluruh data harus berupa angka                            |
|   2 | Input tidak valid – ujian       | `ujian < 0` atau `ujian > 100`                          | `105, 80, 90`                            | Masukkan ditolak: nilai ujian di luar rentang 0 sampai 100                   |
|   3 | Input tidak valid – tugas       | `tugas < 0` atau `tugas > 100`                          | `80, -5, 90`                             | Masukkan ditolak: nilai tugas di luar rentang 0 sampai 100                   |
|   4 | Input tidak valid – kehadiran   | `hadir < 0` atau `hadir > 100`                          | `80, 80, 105`                            | Masukkan ditolak: kehadiran di luar rentang 0 sampai 100                     |
|   5 | Tidak memenuhi syarat kehadiran | `hadir < 80`                                            | `90, 90, 75`                             | Nilai akhir tetap ditampilkan, tetapi status tidak memenuhi syarat kehadiran |
|   6 | Predikat A                      | `akhir >= 85` dan `hadir >= 80`                         | `90, 80, 95` → 86.00                     | Predikat A, Lulus                                                            |
|   7 | Predikat B                      | `70 <= akhir < 85` dan `hadir >= 80`                    | `75, 70, 85` → 73.00                     | Predikat B, Lulus                                                            |
|   8 | Predikat C                      | `60 <= akhir < 70` dan `hadir >= 80`                    | `60, 60, 80` → 60.00                     | Predikat C, Lulus                                                            |
|   9 | Predikat D                      | `50 <= akhir < 60` dan `hadir >= 80`                    | `55, 50, 90` → 53.00                     | Predikat D, Belum lulus                                                      |
|  10 | Predikat E                      | `akhir < 50` dan `hadir >= 80`                          | `40, 30, 100` → 36.00                    | Predikat E, Belum lulus                                                      |

## Hasil Pengujian
| No. | Ujian | Tugas | Kehadiran | Nilai Akhir yang Diharapkan | Keluaran yang Diharapkan                                         | Nilai Akhir Aktual | Keluaran Aktual                                                  | Status |
| --: | ----: | ----: | --------: | --------------------------: | ---------------------------------------------------------------- | -----------------: | ---------------------------------------------------------------- | ------ |
|   1 |    90 |    80 |        95 |                       86.00 | Predikat A, Lulus                                                |              86.00 | Predikat A, Lulus                                                | Sesuai |
|   2 |    75 |    70 |        85 |                       73.00 | Predikat B, Lulus                                                |              73.00 | Predikat B, Lulus                                                | Sesuai |
|   3 |    60 |    60 |        80 |                       60.00 | Predikat C, Lulus                                                |              60.00 | Predikat C, Lulus                                                | Sesuai |
|   4 |    55 |    50 |        90 |                       53.00 | Predikat D, Belum lulus                                          |              53.00 | Predikat D, Belum lulus                                          | Sesuai |
|   5 |    40 |    30 |       100 |                       36.00 | Predikat E, Belum lulus                                          |              36.00 | Predikat E, Belum lulus                                          | Sesuai |
|   6 |    90 |    90 |        75 |                       90.00 | Nilai akhir tetap tampil, status tidak memenuhi syarat kehadiran |              90.00 | Nilai akhir tetap tampil, status tidak memenuhi syarat kehadiran | Sesuai |
|   7 |   105 |    80 |        90 |                           - | Pesan penolakan rentang nilai ujian                              |                  - | Pesan penolakan rentang nilai ujian                              | Sesuai |
|   8 |    80 |    -5 |        90 |                           - | Pesan penolakan rentang nilai tugas                              |                  - | Pesan penolakan rentang nilai tugas                              | Sesuai |
|   9 |    80 |    80 |       abc |                           - | Pesan penolakan tipe                                             |                  - | Pesan penolakan tipe                                             | Sesuai |

## Refleksi
Jelaskan satu masukan tidak valid yang semula terlewat dan cara menanganinya.

## Bukti Pengujian Penilaian Praktik 1

| Masukkan | Keluaran diharapkan | Keluaran aktual | Status |
|---|---|---|---|
| 92 | Predikat A | Predikat A | Sesuai |
| 85 | Predikat A | Predikat A | Sesuai |
| 84.9 | Predikat B | Predikat B | Sesuai |
| 49.9 | Predikat E | Predikat E | Sesuai |
| -1 | Pesan penolakan rentang | Pesan penolakan rentang | Sesuai |
| abc | Pesan penolakan tipe | Pesan penolakan tipe | Sesuai |