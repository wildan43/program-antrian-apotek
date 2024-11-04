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
        tp = self.headval
        while tp.nextval != None:
            tp = tp.nextval
        newNode = node(y)
        tp.nextval = newNode



    def print(self):
        p = self.headval
        print(">> method print dijalankan:")
        while p != None:
            print(p.dataval,"-->",end="")
            p = p.nextval
        print("|")        
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
L.insertdepan(14)
L.print()
#