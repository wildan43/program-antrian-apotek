#J0403221073_Fatih Kawakib Kartono_TPLB2_PERTEMUAN8

# fungsi merge_sort
def merge_sort(alist):
    # print isi list pada setiap rekursif
    print("Membagi", alist, end="\n", sep="       ---> ")
    
    # base case: jika panjang list <= 1, maka list sudah terurut
    if len(alist) <= 1:
        return alist
    
    # rekursif: membagi list menjadi 2 bagian
    mid = len(alist) // 2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]
    
    # memanggil rekursif untuk membagi bagian kiri dan kanan
    merge_sort(lefthalf)
    merge_sort(righthalf)
    
    # proses merging
    i = 0  # indeks untuk lefthalf
    j = 0  # indeks untuk righthalf
    k = 0  # indeks untuk alist
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k] = lefthalf[i]
            i += 1
        else:
            alist[k] = righthalf[j]
            j += 1
        k += 1

    # memasukkan sisa elemen yang belum terpasang ke dalam list
    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        alist[k] = righthalf[j]
        j += 1
        k += 1
    
    # print proses merging pada setiap rekursif
    print("Menggabungkan", alist, end="\n", sep=" ---> ")

# contoh penggunaan
alist = [16, 82, 7, 45, 98, 61, 10, 29, 73]
merge_sort(alist)
print("\nHasil akhir", alist, end="\n ", sep="      : ")