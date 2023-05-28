
class Universitas: #Class ketiga yaitu universitas 
    def __init__(self, nama_universitas): #inisialisasi atribut NamaUniversitas dan DaftarJurusan
        #atribut nama  universitas dan daftar jurusan 
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = [] #menginisialisasi atribut DaftarJurusan sebagai sebuah list kosong.
    
   # menambahkan objek Jurusan ke dalam DaftarJurusan
    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)
    
        print("-----------------------") #membuat pemisah 
    #menampilkan daftar jurusan yang ada di Universitas
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan yang ada di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            #memanggil nama jurusan 
            print("Nama Jurusan:", jurusan.NamaJurusan)
            print("-----------------------")


