class Jurusan:
    def __init__(self, nama_jurusan): # Inisialisasi atribut nama_jurusan dan DaftarMahasiswa
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = [] #menginisialisasi atribut DaftarMahasiswa sebagai sebuah list kosong.
    
    def tambah_mahasiswa(self, mahasiswa):
    #menambahkan objek Mahasiswa ke dalam DaftarMahasiswa 
        self.DaftarMahasiswa.append(mahasiswa)
    
    def tampilkan_daftar_mahasiswa(self):
       # menampilkan daftar mahasiswa yang terdaftar dalam Jurusan
        print("Daftar Mahasiswa yang ada di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa: #merepresentasikan objek mahasiswa 
            print("Nama Mahasiswa:", mahasiswa.nama) #memanggil nama mahasiswa
            print("NIM Mahasiwa:", mahasiswa.nim) #memanggil nim mahasiswa
            print("-----------------------") # mencetak - untuk lebih rapi