kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

# Mata kuliah yang diambil kedua kelas
mata_kuliah_kedua_kelas = kelas_A.union(kelas_B) #union fungsinya untuk menggabungkan dua bagian set
print("Mata kuliah yang diambil kedua kelas:")
print(mata_kuliah_kedua_kelas)

# Mata kuliah yang hanya diambil kelas A
mata_kuliah_kelas_A = kelas_A.difference(kelas_B) #difference fungsinya untuk mencari perbedaan 
print("Mata kuliah yang hanya diambil kelas A:")
print(mata_kuliah_kelas_A)

# Mata kuliah unik yang diambil kedua kelas
mata_kuliah_unik = kelas_A.symmetric_difference(kelas_B) #fungsi dari symmetric_difference cara mencari elemen yang unik di antara dua set
print("Mata kuliah unik yang diambil kedua kelas:")
print(mata_kuliah_unik)