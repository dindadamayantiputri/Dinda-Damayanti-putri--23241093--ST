def main():
    print("Selamat datang di permainan Tebak Angka!")
    
    # Meminta satu pengguna untuk memasukkan angka rahasia
    angka_rahasia = int(input("Masukkan angka rahasia antara 1 dan 100: "))
    
    # Validasi angka rahasia agar berada di antara 1 dan 100
    while angka_rahasia < 1 or angka_rahasia > 100:
        print("Angka harus berada di antara 1 dan 100. Coba lagi.")
        angka_rahasia = int(input("Masukkan angka rahasia antara 1 dan 100: "))
    
    tebakan = None
    percobaan = 0
    
    print("Pengguna lain, sekarang coba tebak angka tersebut!")
    
    # Perulangan while untuk meminta pengguna menebak hingga benar
    while tebakan != angka_rahasia:
        # Meminta input dari pengguna
        tebakan = int(input("Masukkan tebakan Anda: "))
        percobaan += 1

        # Percabangan if-else untuk memberi petunjuk kepada pengguna
        if tebakan < angka_rahasia:
            print("Terlalu rendah! Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Terlalu tinggi! Coba lagi.")
        else:
            print(f"Selamat! Anda menebak dengan benar dalam {percobaan} percobaan.")
            break

    print("Terima kasih telah bermain!")

# Memanggil fungsi utama untuk menjalankan program
if __name__ == "__main__":
    main()
