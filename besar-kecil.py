# Testing algoritma mengurutkan bilangan dari terbesar ke yang terkecil
# ALPO1B1P0106
# 1. Perhatikan bilangan yang ada
# 2. Coba bandingkan bilangan yang bersandingan
# 3. Jika ingin diurutkan dari terbesar bandingkan bilangan yang bersandingan dari kiri ke kanan
# 4. Jika bilangan sebelah kanan lebih besar dari dari sebelah kiri maka tukar posisi bilangan tsb
# 5. Jika ingin diurutkan dari terkecil bandingkan bilangan yang bersandingan dari kiri ke kanan
# 6. Jika bilangan sebelah kanan lebih kecil dari dari sebelah kiri maka tukar posisi bilangan tsb
# 7. Lanjutkan langkah di atas hingga bilangan terakhir
# 8. Jika sudah mentok ulangi lagi langkahnya sampai tidak ada lagi bilangan yang perlu ditukar posisinya
# 9. Akan didapatkan hasil 82, 79, 56, 23, 18 diurutkan dari yang terbesar
# 10. Akan didapatkan hasil 18, 23, 56, 79, 82 diurutkan dari yang terkecil
# 11. Sehingga diketahui juga nilai terbesar 82, nilai terkecil 18

# menampilkan bilangan sesuai soal
bilangan = [82, 56, 23, 18, 79]
print('\n', bilangan, '\n')

# membuat fungsi untuk membandingkan antar bilangan dan mengurutkan dari terbesar ke terkecil
def terbesar(bilangan):
    n = len(bilangan)
    for a in range(n):
        swapped = False
        for b in range(0, n-a-1):
            if bilangan[b] < bilangan[b+1]:
                bilangan[b], bilangan[b+1] = bilangan[b+1], bilangan[b]
                swapped = True
        # Jika tidak ada pertukaran maka bilangan sudah terurut
        if not swapped:
            break
    return bilangan

# membuat fungsi untuk membandingkan antar bilangan dan mengurutkan dari terkecil ke terbesar
def terkecil(bilangan):
    n = len(bilangan)
    for a in range(n):
        swapped = False
        for b in range(0, n-a-1):
            if bilangan[b] > bilangan[b+1]:
                bilangan[b], bilangan[b+1] = bilangan[b+1], bilangan[b]
                swapped = True
        # Jika tidak ada pertukaran maka bilangan sudah terurut
        if not swapped:
            break
    return bilangan

# output hasil urutan bilangan dari yang terbesar
hasil_terbesar = terbesar(bilangan)
print('Diurutkan dari yang terbesar:', hasil_terbesar)

# output hasil urutan bilangan dari yang terkecil
hasil_terkecil = terkecil(bilangan)
print('Diurutkan dari yang terkecil:', hasil_terkecil)

# output nilai terbesar dari urutan bilangan yang ada
bilmaks = terbesar(bilangan)[0]
print('Nilai terbesar:',bilmaks)

# output nilai terkecil dari urutan bilangan yang ada
bilmin = terkecil(bilangan)[0]
print('Nilai terkecil:',bilmin,'\n')