# Testing algoritma menentukan bilangan ganjil & genap
# ALPO1B1P0105

# 1. Perhatikan bilangan yang ada
# 2. Bagilah bilangan dengan angka 2 (misalnya 56 ÷ 2 = 28, sisa pembagian = 0)
# 3. Perhatikan sisa pembagiannya
# 4. Jika sisa pembagian adalah 0/habis dibagi 2, maka bilangan tersebut genap
# 5. Jika sisa pembagian bukan 0, maka bilangan tersebut ganjil
# 6. Akan didapatkan bilangan ganjil = 23, 79, dan bilangan genap = 18, 56, 82

# menampilkan bilangan sesuai soal
bilangan = [82, 56, 23, 18, 79]
print('\n',bilangan,'\n')

# bilangan dibagi 2 serta menampilkan sisa pembagian
n = 2 
for nilai in bilangan:
    print(nilai,'÷',n,'=',nilai // n,'| sisa pembagian =', nilai % n)
# penentuan bilangan ganjil / genap
    if nilai % n == 0:
        print('maka', nilai, 'merupakan bilangan genap\n')
    else:
        print('maka', nilai, 'merupakan bilangan ganjil\n')