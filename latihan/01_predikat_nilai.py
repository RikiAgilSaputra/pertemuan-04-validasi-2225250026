nilai = float(input("Masukkan Nilai Akhir (0-100):"))

if nilai > 100 or nilai < 0:
      print ("Masukkan nilai dengan rentang 0-100")
else:
      if nilai >= 85:
       predikat = "A"
      elif nilai >= 70:
       predikat = "B"
      elif nilai>= 60:
       predikat = "C"
      elif nilai >= 50:
       predikat = "D"
      else:
       predikat = "E"

      print (f"Nilai {nilai:.2f} memperoleh predikat {predikat}")
