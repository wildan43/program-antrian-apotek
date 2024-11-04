print ("==============")
print (" WILDAN HOLIK ")
print (" J0403221025  ")
print ("==============")

def mergeSort(L): #Definisi fungsi mergesort dengan parameter L
    print("Splitting ",L)
    if len(L)>1: #Jika panjang L lebih dari satu
        mid = len(L)//2 #Maka bagi L menjadi dua bagian
        lefthalf = L[:mid] #Variable lefthalf yaitu bagian kiri dari L
        righthalf = L[mid:] #Variable righthalf yaitu bagian kanan dari L

        mergeSort(lefthalf) #panggil mergesort dengan variabel lefthalf
        mergeSort(righthalf) #panggil mergesort dengan variabel righthalf

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf): #pengulangan i apabila lebih kecil dari panjang lefthalf dan j lebih kecil dari panjang righthalf
            if lefthalf[i] <= righthalf[j]: #Jika lefthalf i lebih kecil dari pada sama dengan righthalf j maka
                L[k]=lefthalf[i]
                i=i+1
            else:
                L[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            L[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            L[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",L)

L = [45,15,105,8,66,29,56]
mergeSort(L)
print(L)
