# inputan dari user
coba = input("masukkan nama : ")
print ("coba: ",coba, "tipe datanya: ",type(coba))

# aritmatika
x = 9
y = 3

# penjumlahan
hasil = x+y
print (x, "+", y, "=", hasil)

# pengurangan
hasil = x-y
print (x, "-", y, "=", hasil)

# perkalian
hasil = x*y
print (x, "x", y, "=", hasil)

# pembagian
hasil = x/y
print (x, ":", y, "=", hasil)

# exponen (perpangkatan)
hasil = x**y
print (x, "^", y, "=", hasil)

# modulus (sisa bagi)
hasil = x%y
print (x, "Mod", y, "=", hasil)

# floor division (pembulatan kebawah)
hasil = x//y
print (x, "//", y, "=", hasil)

# aritmatika prioritas
# (), exponen, perkalian, penjumlahan, pengurangan
x = 3
y = 4
z = 5
hasil = (x ** y * z + x / y - z % x // y)
print (x, "**", y, "*", z, "+", x, "/", y, "-", z, "%", x, "//", y, "=", hasil)