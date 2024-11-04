#A = ("apple","banana","cherry","apple","banana","banana","apple")
#print(len(A))

#x = {"apple","banana","cherry"}
#y = {"google","microsoft","apple"}
#z = x.symmetric_difference (y)
#print (z)

#c ={"brand":"Ford","model":"Mustang","year":1964}
#for x in c:
    #print(x,end="#")

#D ={"brand":"Ford","model":"Mustang","year":1964}
#for x in D.values():
    #print(x,end=" ")

#def fibo (n):
    #if n==1 or n==2:
        #return 1
    #else:
        #return fibo (n-1)+fibo(n-2)
    
#n=10
#print(fibo(n))

def fibo (n):
    if n==1 or n==2:
        return 1
    else:
        return fibo (n-1)+fibo(n-2)
    
n=5
print(fibo(5))