class node:
    def __init__(self,x):
        self.dataval = x
        self.nextval = None


class linkedlist:
    def __init__(self):
        self.headval = None

    def insertdepan(self,y):
        newNode = node(y)
        print(">> method insert node di depan dijalankan: data - ",newNode.dataval)
        if self.headval == None:
            self.headval = newNode
        else:
            newNode.nextval = self.headval
            self.headval = newNode

    def insertbelakang(self,y):
        newNode = node(y)
        if self.headval != None:#LL sudah ada nodenya
            tp = self.headval
            while tp.nextval != None:
                tp = tp.nextval
            tp.nextval = newNode
        else:#LL masih kosong (belum ada nodenya)
            self.headval = newNode

    def print(self):
        p = self.headval
        print(">> method print dijalankan:")
        while p != None:
            print(p.dataval,"-->",end="")
            p = p.nextval
        print("|") 
    
    def len(self):
        p = self.headval
        jmlhnode = 0
        while p != None:
            jmlhnode += 1
            p = p.nextval
        return jmlhnode    

    def insert(self,n,y): #memasukan dataval y, di posisi node ke n
        #urutan posisi n dari 0
        if n == 0:
            self.insertdepan(y)
        elif n == self.len():
            self.insertbelakang(y)
        elif n>0 and n< self.len():
            pb =self.headval
            for i in range(n-1):
                pb = pb.nextval
            #print("n:",n,"-->pb megang:",pb.dataval)
            newNode = node(y)
            newNode.nextval = pb.nextval
            pb.nextval = newNode   
        else:
            print("nilai n:",n,"tidak valid, n yang boleh hanya dari 0 sd",self.len()) 

'''
andaikan alamat node pertama (yg isinya 3) 002FF3
andaikan alamat node kedua (yg isinya 1) 00FFF5
alamat node ketiga (yg isinya 4) 44FF4
alamat node keempat (yg isinya 10) AAFFA

p itu isinya 002FF3 (alamat node yang ditunjuk headval)
headval juga isinya 002FF3
apakah p !=None? YA TRUE
  berarti baris 20 dikerjain ---> dicetak 3
  p isinya diminta diganti oleh p.nextval yang sedang berisi 00FFF5
  alias alamat node yang kedua
  isi p akan menjadi = 00FFF5 sekarang jadi nunjuk alamat node kedua
 
apakah p !=None? YA TRUE
    nyetak angka 1
    p berubah 44FF4 yang notabene alamat node ketiga yang isi data 4

apakah p !=None? YA TRUE
    nyetak angka 4
    p jadi AAFFA (alamat node ke 4 dari depan)

apakah p !=None? YA TRUE
    nyetak 10
    p akan menjadi None    

apakah p !=None? TIDAK

'''

L = linkedlist()
#print(L.headval)
L.insertdepan(10)
L.print()
L.insertdepan(4)
L.insertdepan(1)
L.insertdepan(3)

L.print()
L.insertbelakang(14)
L.print()

print(L.len())
L.insert(3,100)
L.print()
L.insert(10,77)
L.print()
#