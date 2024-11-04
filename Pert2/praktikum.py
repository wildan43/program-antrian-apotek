class mobil:
    def __init__(self,m,mo,p,w,t=None):
        self.merk =m
        self.model=mo
        self.plat =p
        self.warna=w
        self.tahun=t

    def info(self):
        print("INFO DETAIL:", self.merk, self.model, self.plat, self.warna, self.tahun)

m1 = mobil("toyota","Avanza","F1A","Hitam","2013")
m2 = mobil("Mitsubushi","Pajero","B1RF")
print(type(m1), m1.merk)
print(m2.model)
m2.info()
m2.warna = "merah"
m2.info()
