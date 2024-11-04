print ("==============")
print (" WILDAN HOLIK ")
print (" J0403221025  ")
print ("==============")

print("================================================================")

print("SquentialSearch")

def Squentialsearch(data, nilai):
    index = []
    for i in range(len(data)):
        if data[i] == nilai:
            index.append(i)
    return index

def LebihBesar(data, nilai):
    index = []
    for i in range(len(data)):
        if data[i] > nilai:
            index.append(i)
    return index

data = [25, 69, 15, 2, 42, 87, 33, 67, 100, 9]
z = 33

x = Squentialsearch(data, z)
y = LebihBesar(data, z)

print(data)
print("Value yang sama dengan {} berada di indeks ke: {}".format(z, x))
print("Value yang lebih besar dari {} berada di indeks ke: {}".format(z, y))

print("================================================================")

print("BinarySearch")

def binary_search(data, x):
    low = 0
    high = len(data) - 1
    result = []
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == x:
            result.append(mid)
            i = mid - 1
            while i >= 0 and data[i] == x:
                result.append(i)
                i -= 1
            i = mid + 1
            while i < len(data) and data[i] == x:
                result.append(i)
                i += 1
            return result
        elif data[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result

def greater_than(data, x):
    low = 0
    high = len(data) - 1
    result = []
    while low <= high:
        mid = (low + high) // 2
        if data[mid] > x:
            result.append(mid)
            high = mid - 1
        else:
            low = mid + 1
    return result

data = [25, 69, 15, 2, 42, 87, 33, 67, 100, 9]
data.sort()
x = 33

print(data)
print(f"~ Value yang sama dengan {x} berada pada indeks : {binary_search(data, x)}")
print(f"~ Value yang lebih besar dari {x} berada pada indeks : {greater_than(data, x)}")

print("================================================================")


