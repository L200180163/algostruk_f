class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTif("diah", 10, "Sukoharjo", 240000)
c1 = MhsTif("siwi", 51, "Sragen", 230000)
c2 = MhsTif("amanda", 2, "Surakarta", 250000)
c3 = MhsTif("Chandra", 18, "Surakarta", 235000)
c4 = MhsTif("brian", 4, "Boyolali", 240000)
c5 = MhsTif("nopal", 31, "Salatiga", 250000)
c6 = MhsTif("fandi", 13, "Klaten", 245000)
c7 = MhsTif("fauzi", 5, "Wonogiri", 245000)
c8 = MhsTif("putri", 23, "Klaten", 245000)
c9 = MhsTif("nimas", 64, "Karanganyar", 270000)
c10 = MhsTif("dewi", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

# 8

def binSearching(kumpulan, target):
    #Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) -1

    #Secara berulang belah runtutan itu menjadi separuhnya
    #sampai targetnya ditemukan
    while low <= high:
        #Temukan pertengahan runtut itu
        mid = (high + low) //2
        #Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            return mid
        elif kumpulan[mid] < target:
            high = mid +1
        else :
            low = mid -1
            
    return -1

b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

