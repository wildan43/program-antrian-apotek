print ("==============")
print (" WILDAN HOLIK ")
print (" J0403221025  ")
print ("==============")


#Definisi fungsi mergesort
def mergesort(L):
    #Print isi list pada setiap rekursif
    print("Membagi", L, end="\n", sep="       ---> ")
    
    #Base case: jika panjang list <= 1, maka list sudah terurut
    if len(L) <= 1:
        return L
    
    #Rekursif: membagi list menjadi 2 bagian
    mid = len(L) // 2
    lefthalf = L[:mid]
    righthalf = L[mid:]
    
    #Memanggil rekursif untuk membagi bagian kiri dan kanan
    mergesort(lefthalf)
    mergesort(righthalf)
    
    #Proses merging
    i = 0  #Indeks untuk lefthalf
    j = 0  #Indeks untuk righthalf
    k = 0  #Indeks untuk L
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            L[k] = lefthalf[i]
            i += 1
        else:
            L[k] = righthalf[j]
            j += 1
        k += 1

    #Memasukkan sisa elemen yang belum terpasang ke dalam list
    while i < len(lefthalf):
        L[k] = lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        L[k] = righthalf[j]
        j += 1
        k += 1
    
    #Print proses merging pada setiap rekursif
    print("Menggabungkan", L, end="\n", sep=" ---> ")

#Contoh impelentasinya
L = [45,15,105,8,66,29,56]
mergesort(L)
print("\nHasil akhir", L, end="\n ", sep="      : ")