# Testing algoritma menentukan bilangan ganjil & genap
# ALPO1B1P0105

# 1. Perhatikan bilangan yang ada
# 2. Coba pilih salah satu bilangan
# 3. Bagilah bilangan yang dipilih dengan angka 2 (misalnya, 79 ÷ 2 = 39, sisa pembagiannya 1, karena 39 × 2 + 1 = 79)
# 4. Perhatikan sisa pembagiannya
# 5. Jika sisa pembagian adalah 0/habis dibagi 2, maka bilangan tersebut genap
# 6. Jika sisa pembagian bukan 0, maka bilangan tersebut ganjil

# menampilkan bilangan
print('82, 56, 23, 18, 79')
# nomor = [82,56,23,18,79]

# memilih salah satu bilangan
bilangan = int (input('pilih salah satu bilangan di atas: '))

#if bilangan == nomor:
#    print('anda memasukkan angka: {bilangan}')
#else:
#    print('masukkan bilangan yang tersedia!')

# bilangan dibagi 2 serta menampilkan sisa pembagian dan alasannya
n = 2 
hasilbagi = bilangan // n
sisabagi = bilangan % n
perhitungan = bilangan // n * n + bilangan % n

print('hasil pembagian: ',bilangan,'/',n,'=',hasilbagi,'| sisa pembagian =', sisabagi,'| karena: ',hasilbagi,'x',n,'+',sisabagi,'=',perhitungan) 
print('karena sisa pembagian =',sisabagi)

# penentuan bilangan ganjil / genap
if bilangan % 2 == 0:
    print('maka', bilangan, 'merupakan bilangan genap')
else:
    print('maka', bilangan, 'merupakan bilangan ganjil')

    # THE END