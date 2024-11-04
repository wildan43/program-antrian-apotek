print ("==============")
print (" WILDAN HOLIK ")
print (" J0403221025  ")
print ("==============")

class stack:
    def __init__(self, n=5):
        self.size = n
        self.number_items_in_stack = 0
        self.top = -1
        self.data = []
    
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

    def push(self, x): 
        print(">> Push:",x)
        if not self.isFull():
            self.data.append(x)
            self.setCurrentNumberItems(self.getCurrentNumberItems()+1)
            self.top = self.getCurrentNumberItems() - 1
        else:
            print("Stack is Full, STACK OVERFLOW!,",x,"gagal dipush.")
    
    def pop(self):
        print(">> POP")
        result = None
        if not self.isEmpty():
            result = self.data.pop()
            self.setCurrentNumberItems(self.getCurrentNumberItems()-1)
            self.top = self.getCurrentNumberItems() - 1
        else:
            print("Stack is empty, STACK UNDERFLOW!, gagal dipop.")
        return result

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

Stack = stack(6)
Stack.print()
Stack.push("7")
Stack.push("10")
Stack.push("13")
Stack.print()