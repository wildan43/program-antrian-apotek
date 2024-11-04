class node:
    def __init__(self,x=None):
        self.data_val = x
        self.next_val = None

class linkedlist:
    def __init__(self):
        self.head=None

x = node(3); print(x,x.data_val,x.next_val)
y = node(1); print(y,y.data_val,y.next_val)

L = linkedlist()
L.head = x 
L.head.next_val=y 
print(L.head.data_val)
print(L.head.next_val)
print(L.head.next_val.data_val)

z = node(7)
y.next_val = z
#L.head.next_val.next_val = z

pos = L.head;
while pos !=None:
    print(pos.data_val)
    pos = pos.next_val