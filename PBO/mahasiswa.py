#Nama : Wahyu Ozorah Manurung 
#NPM : G1A022060
#TUGAS PBO

    # Pada tugas OOP ini diminta membuat 3 kelas object yaitu class mahasiswa,  class jurusan, class universitas dan  saya menggunakan 4 file 
    # pada kode nya yaitu 3 file untuk masing-masing class dan 1 file yaitu main untuk me run class dan sesuai yang diminta pada pertanyaan. 

class Mahasiswa: #class pertama yaitu class mahasiswa 
    def __init__(self, nama, nim, jurusan): # fungsi untuk inisialisasi atribut
        # Inisialisasi atribut nama, nim, dan jurusan
        self.nama = nama 
        self.nim = nim 
        self.jurusan = jurusan 
    
    def tampilkan_info(self): #Fungsi untuk menampilkan info
         # Menampilkan informasi mahasiswa
        print("Nama Mahasiswa:", self.nama)
        print("NIM Mahasiswa:", self.nim)

        # Jika mahasiswa memiliki jurusan, tampilkan nama jurusan
        if self.jurusan is not None:
            print("Jurusan Mahasiswa:", self.jurusan.NamaJurusan) #Memanggil nama jurusan mahasiswa