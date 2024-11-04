def merge_sort(arr):
    # jika panjang array kurang dari atau sama dengan 1, kembalikan array tersebut
    if len(arr) <= 1:
        return arr

    # bagi array menjadi dua bagian
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # rekursif memanggil merge_sort() untuk kedua bagian
    left = merge_sort(left)
    right = merge_sort(right)

    # gabungkan kedua bagian yang sudah terurut menjadi satu array hasil penggabungan
    return merge(left, right)


def merge(left, right):
    result = []  # array hasil penggabungan
    i, j = 0, 0  # indeks untuk kedua bagian

    # bandingkan elemen-elemen dari kedua bagian dan tambahkan elemen dengan nilai terkecil pada array hasil penggabungan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # tambahkan sisa elemen dari bagian yang belum habis pada array hasil penggabungan
    result += left[i:]
    result += right[j:]

    return result


# contoh penggunaan merge_sort()
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)

merge_sort([38, 27, 43, 3, 9, 82, 10])
# len([38, 27, 43, 3, 9, 82, 10]) > 1, maka array dibagi menjadi dua bagian:
# left=[38
