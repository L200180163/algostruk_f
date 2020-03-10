from Latihan23 import Manusia
class Mahasiswa(Manusia):
    """class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.NIM = nim
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama +', NIM '+str(self.NIM) \
            +'. Tinggal di '+self.kotaTinggal \
            +'. Uang saku Rp '+str(self.uangSaku) \
            +' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, kota):
        self.kotaTinggal = kota
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self, tambahan):
        self.uangSaku = self.uangSaku + tambahan
    def makan(self, s):
        """Metode ini menutupi 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan ",s," sambil belajar")
        self.keadaan = 'kenyang'

# ada kelanjutannya (Lihat di "Soal-soal untuk Mahasiswa").
