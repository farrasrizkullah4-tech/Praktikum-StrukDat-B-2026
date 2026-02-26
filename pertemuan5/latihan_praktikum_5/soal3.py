# 3. Diberikan dua daftar hadir mahasiswa di dua sesi yang berbeda:
sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}
# a. Tampilkan nama mahasiswa yang hadir di kedua sesi (pagi DAN siang))
pagi_siang=sesi_pagi.intersection(sesi_siang)
print(pagi_siang)
# b. Tampilkan total daftar nama unik yang hadir hari itu (semua mahasiswa dari kedua sesi tanpa duplikat).
pagi_siang=sesi_pagi.symmetric_difference(sesi_siang)
print(pagi_siang)
# c. Gabungkan kedua set tersebut menjadi satu set bernama sesi_hari_ini.
sesi_hari_ini=(sesi_pagi) | (sesi_siang)
print(sesi_hari_ini)