# 1. Diberikan list nilai mahasiswa: nilai_tugas = [70, 85, 90, 65, 80]   
nilai_tugas = [70, 85, 90, 65, 80]
# a. Ganti nilai 65 menjadi 75 menggunakan pencarian indeks.
nilai_tugas[3]= 75
# b. Tambahkan nilai 95 ke dalam list, lalu urutkan list tersebut dari yang terbesar ke terkecil.
nilai_tugas.append(95)
nilai_tugas.sort(reverse = True)
print(nilai_tugas)
# c. Tampilkan jumlah total seluruh nilai dalam list tersebut.
nilai_tugas = len(nilai_tugas)
print(nilai_tugas)
# d. Tampilkan pesan "Ada nilai sempurna" jika angka 100 ada di dalam list, jika tidak tampilkan "Tidak ada”. 
nilai_sempurna = 100
nilai_tugas = [70, 85, 90, 65, 80]
if 100 in nilai_tugas:
    print("Ada nilai sempurna")
else:
    print("Tidak ada")




