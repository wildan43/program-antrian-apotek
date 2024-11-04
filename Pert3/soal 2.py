class Node:#class dengan nama Node
    def __init__(self,dataval=None) : #Definisi fungsi __init__ menggunakan parameter self dan dataval dengan value none
        self.dataval = dataval #Parameter self.dataval menyimpan nilai variabel dataval
        self.nextval = None #Parameter self.nextval menyimpan nilai variabel dataval
class SlinkedList:#class dengan nama SLinkedList
    def __init__(self) :#Definisi fungsi __init__ menggunakan parameter self
        self.headval=None #Parameter self.headval menyimpan nilai none
    def listprint(self) :#Definisi fungsi listprint menggunakan menggunakan parameter self
        printval=self.headval #Parameter self.headval menyimpan nilai variabel printval
        while printval is not None :#Loop variabel printval jika tidak sama dengan none 
            print(printval.dataval,"-->",end="") #Mencetak printval.dataval       
            printval = printval.nextval #Jika putaran terus terjadi printval akan diubah menjadi nextval
        print("NULL") #Mencetak "NULL"

    def insertdepan(self, x): #fungsi dari insertdepan untuk menambahkan bagian depan                        
        newNode = Node (x) #Node baru untuk menyimpan nilai                            
        newNode.nextval = self.headval #nilai dari Node baru disimpan di headval
        self.headval = newNode  #Node baru menjadi headval                        
        
    def insertbelakang (self, x) : #fungsi dari insertdepan untuk menambahkan bagian depan                     
        newNode = Node (x) #Node baru untuk menyimpan nilai                              
        if self.headval is None : #Melakukan loop apabila headval none                      
            self.headval = newNode #Node baru ditambahkan diakhir                    
        else :
            x = self.headval   #Nilai self headval akan disimpan di x                         
            while x.nextval != None : #Melakukan loop apabila x.nextval tidak sama dengan none                
                x = x.nextval #node terakhir dihubungkan dengan node selanjutnya                          
            x.nextval = newNode  #node baru dari x.nextval         

list1 = SlinkedList()#Variabel list1 merupakan class baru di SLinkedList
list1.headval= Node(1)#Variabel list.headval akan mencetak Node dengan nilai 1
e2 =Node(3) #e2 merupakan suatu class dengan nilai 3
e3= Node(4) #e3 merupakan suatu class dengan nilai 4
e4= Node(10)#e4 merupakan suatu class dengan nilai 10

list1.headval.nextval=e2 #Mengubah headval menjadi nextval dengan nilai e2
e2.nextval=e3 #Mengubah e2 dengan nextval dengan nilai e3
e3.nextval=e4 #Mengubah e3 dengan nextval dengan nilai e4
list1.insertdepan(5) #Variabel list1 memanggil insertdepan yang berisi 5                                  
list1.insertbelakang(30) #Variabel list1 memanggil insertbelakang yang berisi 30 
list1.listprint() #Cetak semua yang ada pada list1     