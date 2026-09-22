a = float(input("Sudut A:"))
b = float(input("Sudut B:"))
c = float(input("Sudut C:"))

if a <= 0 or c <= 0 or c <= 0:
    print("Masukkan ditolak: Setiap sudut harus lebih besar dari 0 derajat")
elif abs (a + b + c - 180) > 1e-9:
    print ("Masukkan ditolak: Jumlah ketiga sudut harus 180 derajat")
else:
    terbesar = max (a, b, c)
    if terbesar > 90:
        print ("sudut tumpul")
    elif terbesar == 90:
        print ("sudut siku-siku")
    else:
        print ("sudut lancip")
    