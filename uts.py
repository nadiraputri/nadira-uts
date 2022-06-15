class pendaftaran:
    def __init__(self, nama, nisn, asal_sekolah, jenis_lomba, kategori, htm):
        self.nama = nama
        self.nisn = nisn
        self.asal_sekolah = asal_sekolah
        self.jenis_lomba = jenis_lomba
        self.kategori = kategori
        self.htm = htm

    def keterangan(self):
        keterangan = ""
        if jenis_lomba == "A" or jenis_lomba == "a":
            keterangan = "matematika"
        elif jenis_lomba == "B" or jenis_lomba == "b":
            keterangan == "sains"
        elif jenis_lomba == "C" or jenis_lomba == "c":
            keterangan = "olahraga"

        print("siswa dengan\n nama : {}\n nisn : {}\n asal_sekolah : {}\n".format(self.nama,self.nisn,self.asal_sekolah))
        print("kategori {}".format(keterangan,self.kategori))
        print("htm {}".format(keterangan,self.htm))

#program pendaftaran lomba
nama = input("masukkan nama :")

#jika menggunakan int, maka
nisn = int(input("masukkan nisn :"))

#menentukan asal sekolah
asal_sekolah = input("masukkan asal sekolah :")

#menentukan kategori
kategori = input("masukkan kategori :")

#pembayaran htm menggunakan float, maka
htm = float(input("htm :"))

# A = matematika
# B = sains
# C = olahraga

jenis_lomba = input("pilih lomba [A/B/C]: ")

pendaftaran = pendaftaran(nama, nisn, asal_sekolah, jenis_lomba, kategori, htm)
pendaftaran.keterangan()