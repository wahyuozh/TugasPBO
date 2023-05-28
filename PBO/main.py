#memanggil ketiga class di ketiga file yang telah dibuat berbeda 
from mahasiswa import Mahasiswa
from jurusan import Jurusan
from universitas import Universitas


# Membuat objek universitas
universitas = Universitas("XYZ University")

# Membuat objek jurusan
jurusan1 = Jurusan("Teknik Informatika")
universitas.tambah_jurusan(jurusan1)

# Membuat objek mahasiswa
mahasiswa1 = Mahasiswa("Wahyu Ozorah Manurung", "G1A022060", None)
#  Menambahkan mahasiswa ke jurusan
jurusan1.tambah_mahasiswa(mahasiswa1)

# Menampilkan daftar jurusan di universitas
universitas.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa di jurusan Informatika
jurusan1.tampilkan_daftar_mahasiswa()

