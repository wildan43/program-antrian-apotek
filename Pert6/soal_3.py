print ("==============")
print (" WILDAN HOLIK ")
print (" J0403221025  ")
print ("==============")

class queue:
    def __init__(self, n=5):
        self.kapasitas = n
        self.id_depan= None
        self.id_belakang =None
        self.isi_saat_ini = 0 #kosong
        self.data = [None]*n

    #memasukan item ke queue
    def enqueue(self,x):
        print(">>> ENQUEUE :",x)
        if self.isi_saat_ini < self.kapasitas:
            if self.isi_saat_ini == 0:
                self.id_depan = self.id_belakang = 0
            else:
                self.id_belakang = self.id_belakang + 1
                if self.id_belakang == self.kapasitas:
                    self.id_belakang = 0
            self.data[self.id_belakang] = x
            self.isi_saat_ini = self.isi_saat_ini + 1 
        else: #penuh
            print(x,"gagal dienqueue")

    def dequeue(self):
        if self.isi_saat_ini > 0: #ada isinya
            hasil = self.data[self.id_depan]
            self.id_depan = self.id_depan + 1
            if self.id_depan==self.kapasitas:
                self.id_depan = 0
            self.isi_saat_ini = self.isi_saat_ini - 1
        else:#kosong
            print("Dequeue gagal dilakukan")
            hasil = None
        return hasil
    
    def visualisasi(self):
        for i in range(self.kapasitas):
            print("----------  ",end="",sep="")
        print()
        #yang kosong
        for i in range(self.kapasitas-self.isi_saat_ini):
            print(" %8s >>"%(" "),end="",sep="")
        #yang isi
        for i in range(self.isi_saat_ini):
            print(" %8s >>"%(self.data[self.id_belakang-i]),end="",sep="")
        print(" [Depan] ")
        for i in range(self.kapasitas):
            print("----------  ",end="",sep="")
        print()


q1 = queue(5)

q1.enqueue("BINTANG")
q1.enqueue("BULAN")
q1.enqueue("MATAHARI")
q1.visualisasi()

q1.dequeue()
q1.visualisasi()