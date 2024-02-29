belanja = float(input("Masukkan total belanja: "))
diskon = float(input("Masukkan diskon: "))
total = float(belanja - (belanja * diskon / 100)) 

print("Total yang harus dibayar: ", total)