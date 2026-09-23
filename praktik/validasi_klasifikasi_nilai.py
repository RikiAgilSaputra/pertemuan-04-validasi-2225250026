print ("VALIDASI DAN KLASIFIKASI NILAI AKHIR")

#input data
teks_ujian = input("Nilai ujian (0-100):").strip()
teks_tugas = input("Nilai tugas (0-100):").strip()
teks_hadir = input("Kehadiran dalam persen (0-100):").strip()

#konversi string ke dalam angka
try:
    ujian = float(teks_ujian)
    tugas = float(teks_tugas)
    hadir = float(teks_hadir)

#proses jika value error
except ValueError: 
    print ("Masukkan ditolak: seluruh data harus berupa angka")

else:
    #periksa rentang data
    if not (0 <= ujian <= 100):
        print ("Masukkan ditolak: nilai ujian diluar rentang o sampai 100")

    elif not (0 <= tugas <= 100):
        print ("Masukkan ditolak: nilai tugas diluar rentang 0 sampai 100")

    elif not (0 <= hadir <= 100):
        print ("Masukkan ditolak: kehadiran diluar rentang 0 sampai 100")

    else:
        akhir = 0.6 * ujian + 0.4 * tugas

        print (f"Nilai akhir: {akhir:.2f}")

        if hadir < 80 :
           print("Status: Tidak memenuhi syarat kehadiran.")
        else:
        #periksa predikat
          if akhir >= 85:
            predikat = "A"

          elif akhir >= 70:
            predikat = "B"

          elif akhir >= 60:
            predikat = "C"

          elif akhir >= 50:
            predikat = "D"

          else:
            predikat = "E"

        #periksa status
    
          if predikat in ("A", "B", "C"):
                status = "lulus"

          else:
           status = "belum lulus"

          print (f"selamat, nilai anda adalah {akhir:.2f} dengan predikat {predikat} dan berstatus {status}")


