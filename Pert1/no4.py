#J0403221025
#Wildan Holik

stok = {'mangga':100, 'jeruk':200, 'apel':600}
#Type data koleksi dictionary 'stock' dengan 3 pasang keys dan value

for akey in stok.keys(): #Loop akey di dalam stok keys
    print("key",akey,"berniali", stok[akey])
    #Cetak item key dengan nilai value pairnya
    
for k in stok.keys():#loop k didalam stok keys
    print("k",akey,"berniali", stok[k])
    #Cetak hasil k sesuai dengan value di stok
    
ks= list(stok.keys()) #variabel ks merubah bentuk stok keys kedalam bentuk list
print(ks)#Cetak ks