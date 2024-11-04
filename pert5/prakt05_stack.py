class stack:
    def __init__(self, n=5):
        self.size = n
        self.number_items_in_stack = 0
        self.top = -1
        self.data = []
        print(">> Objek stack dibuat, dengan kapasitas",n)
    
    def info(self):
        print("\n>> Info detail stack")
        print("- kapasitas:",self.size)
        print("- jumlah isi item saat ini:",self.number_items_in_stack)
        if self.top != -1:
            print("- top:",self.top,"-",self.data[self.top]);
        else:
            print("- top: - ");
        print("- list data:",self.data,"\n")
    
    def setSize(self,n):
        self.size = n
    
    def getSize(self):
        return self.size
    
    def getCurrentNumberItems(self):
        return self.number_items_in_stack

    def setCurrentNumberItems(self,n):
        self.number_items_in_stack = n

    def isEmpty(self):
        if self.getCurrentNumberItems()==0:
            return True
        else:
            return False
    
    def isFull(self):
        if self.getCurrentNumberItems() == self.getSize():
            return True
        else:
            return False

    def push(self, x):  #misalkan di stack ada 10 benda, yg keisi idx = 0,1,2,3...9
        print(">> Push:",x)
        if not self.isFull():
            self.data.append(x)
            self.setCurrentNumberItems(self.getCurrentNumberItems()+1)
            self.top = self.getCurrentNumberItems() - 1
        else:
            print("Stack is Full, STACK OVERFLOW!,",x,"gagal di push.")
    
    def pop(self):
        print(">> POP")
        result = None
        if not self.isEmpty():
            result = self.data.pop()
            self.setCurrentNumberItems(self.getCurrentNumberItems()-1)
            self.top = self.getCurrentNumberItems() - 1
        else:
            print("Stack is empty, STACK UNDERFLOW!, gagal di pop.")
        return result

    def multipushs(self,X): #x harus array
        jmlh = len(X)
        for i in range(jmlh):
            self.push(X[i])

    def print(self):
        print("\n>> Print:")
        N = self.getSize()
        for i in range(N-1,-1,-1):
            if i<self.top:
                print("[%2d] | %-10s |"%(i,self.data[i]))
            elif i==self.top:
                print("[%2d] | %-10s |<--TOP"%(i,self.data[i]))
            else:
                print("[%2d] | %10s |"%(i,""))
        print("      ------------")
        print("")

S = stack(7)
S.print()
#S.info()
S.push("KUCING")
S.push("KAMBING")
S.push("KECOA")
S.push("KELINCI")
S.print()
#S.multipushs(["AYAM","BEBEK","ANGSA","BURUNG","ITIK"])
#S.info()
'''hasil = S.pop();print("Hasil pop:",hasil)
hasil = S.pop();print("Hasil pop:",hasil)
hasil = S.pop();print("Hasil pop:",hasil)
hasil = S.pop();print("Hasil pop:",hasil)'''
#S.info()

