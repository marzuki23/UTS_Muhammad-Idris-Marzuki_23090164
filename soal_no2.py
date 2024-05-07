tahun = int(input('Masukkan Tahun : ' ))
if tahun % 400 == 0:
    print("Tahun",tahun,"Merupakan TAHUN KABISAT")
elif tahun % 4 == 0 and tahun % 100 != 0:
    print("Tahun",tahun,"Merupakan TAHUN KABISAT")
else:
    print("Tahun",tahun,"Bukan TAHUN KABISAT")