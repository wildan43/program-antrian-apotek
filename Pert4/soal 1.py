print ("==============")
print (" WILDAN HOLIK ")
print (" J0403221025  ")
print ("==============")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def update(self,heubeul,anyar):
        current = self.head
        while current:
            if current.data == heubeul:
                current.data = anyar
                return
            current = current.next
          
    def print(self):
        z = self.head
        while z !=None:
            print(z.data,"----->",end="")
            z = z.next
        print("|")
            

siji = SLL()
siji.head = Node(2)
dua  = Node(4)
tilu = Node(7)
opat = Node(9)
lima = Node(11)
siji.head.next = dua 
dua.next = tilu
tilu.next = opat 
opat.next = lima
print("===================")
print("Awal sebelum update")
print("===================")
siji.print()
print("===================")
print("Baru setelah update")
print("===================")
siji.update(7, 6)
siji.print()