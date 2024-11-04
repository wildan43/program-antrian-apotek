#J0403221025
#Wildan Holik

dict = {'Name': 'Sara', 'Age': 7}
#Type Data kolektif dictionary 'dict' dengan keys 'Name' dan 'Age' juga memiliki value 'Sara' dan 'Age'
dict2 = {'Sex': 'female', 'Birth': 1998}
#Type Data kolektif dictionary 'dict' dengan keys 'Sex' dan 'Birth' juga memiliki value 'female' dan '1998'

dict3 = {"dict1": dict, "dict2":dict2}
#Type Data kolektif memanggil 'dict' dan 'dict2'
print(dict3) #cetak dict3

dict.update(dict2)#
#tambahkan item 'dict2' kedalam 'dict'
print("Value : %s" % dict)
#cetak value dari 'dict' setelah di update