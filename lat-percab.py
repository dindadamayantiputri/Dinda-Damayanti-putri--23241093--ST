print("Silahkan masukkan operasi yang diinginkan")
print("1 - operasi penjumlahan")
print("2 - operasi pengurangan")
pilihan = input("Masukkan pilihan anda: ")

if pilihan == "1":
        print("Ini operasi penjumlahan")
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        hasil = a+b
        print(f"Hasil adalah: {hasil}")
elif pilihan == "2":
        print("Ini operasi pengurangan")
        c = int(input("Masukkan bilangan pertama: "))
        d = int(input("Masukkan bilangan kedua: "))
        hasil = c-d
        print(f"Hasil adalah: {hasil}")
else:
        print("Pilihan tidak valid")
print("program selesai")