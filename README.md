# Tugas PBO 

NAMA: WAHYU OZORAH MANURUNG

NPM : G1A022060

KELAS  : B

# KASUS 
Andi adalah seorang mahasiswa Informatika yang sedang belajar konsep Pemrograman Berorientasi Objek (PBO) menggunakan bahasa pemrograman Python. Ia ingin membuat program sederhana untuk mengelola data mahasiswa di sebuah universitas. Andi memutuskan untuk membuat tiga kelas objek yang saling berhubungan: Mahasiswa, Jurusan, dan Universitas.

Kelas Mahasiswa:
Kelas Mahasiswa memiliki atribut sebagai berikut:
Nama (string)
NIM (string)
Jurusan (objek dari kelas Jurusan)
Kelas Mahasiswa memiliki metode sebagai berikut:
init(self, nama, nim, jurusan): inisialisasi atribut Nama, NIM, dan Jurusan
tampilkan_info(self): menampilkan informasi Nama, NIM, dan nama Jurusan mahasiswa

Kelas Jurusan:
Kelas Jurusan memiliki atribut sebagai berikut:
NamaJurusan (string)
DaftarMahasiswa (daftar objek Mahasiswa)
Kelas Jurusan memiliki metode sebagai berikut:
init(self, nama_jurusan): inisialisasi atribut NamaJurusan dan DaftarMahasiswa
tambah_mahasiswa(self, mahasiswa): menambahkan objek Mahasiswa ke dalam DaftarMahasiswa
tampilkan_daftar_mahasiswa(self): menampilkan daftar mahasiswa yang terdaftar dalam Jurusan

Kelas Universitas:
Kelas Universitas memiliki atribut sebagai berikut:
NamaUniversitas (string)
DaftarJurusan (daftar objek Jurusan)
Kelas Universitas memiliki metode sebagai berikut:
init(self, nama_universitas): inisialisasi atribut NamaUniversitas dan DaftarJurusan
tambah_jurusan(self, jurusan): menambahkan objek Jurusan ke dalam DaftarJurusan
tampilkan_daftar_jurusan(self): menampilkan daftar jurusan yang ada di Universitas

Andi ingin menggunakan programnya untuk mengelola data mahasiswa dan jurusan di Universitas XYZ.
Bantulah Andi untuk mengimplementasikan tiga kelas objek tersebut agar programnya dapat berjalan dengan baik.

# PERTANYAAN
1.Implementasikan kelas Mahasiswa, Jurusan dan Universitas sesuai dengan spesifikasi yang diberikan.

2.Buatlah sebuah objek Universitas dengan nama "XYZ University".

3.Buatlah objek Jurusan dengan nama "Teknik Informatika" dan tambahkan objek tersebut ke dalam Universitas XYZ.

4.Buatlah objek Mahasiswa dengan nama "Kalian masing", NIM "Kalian masing", dan masukkan ke dalam Jurusan Teknik Informatika di Universitas XYZ.

5.Tampilkan daftar jurusan yang ada di Universitas XYZ.

6.Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ.

# PENJELASAN 
Pada kasus diatas saya menggunakan konsep OOP dengan tiga kelas yang mana ketiga kelas tersebut saya pisahkan di masing-masing file untuk mempermudah saya dalam memahaminya. selanjutnya untuk pertanyaan yang diminta atau implementasi dari yang andi inginkan saya membuat file baru untuk me run kode nya dengan memanggil dari ketiga class di satu file yang saya beri nama " MAIIN"
























