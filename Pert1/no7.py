#J0403221025
#Wildan Holik

dishes=["pizza","sauerkraut","paelia","hambuerger"]
#4 element type data list 
countries=["italy","germany","spain","USA","switzerland"]
#5 element type data 
country_specialities=list(zip(countries, dishes))
#Mengembalikan 2 data list dengan method zip
print(country_specialities)
#Cetak country_specialities
country_specialities_dict=dict(country_specialities)
#Rubah data list menjadi data koleksi dictionary
print(country_specialities_dict)
#Data list yang sudah diubah menjadi data kolektif dictionary