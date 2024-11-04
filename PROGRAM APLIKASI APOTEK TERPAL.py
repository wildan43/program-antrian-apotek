'''
KELOMPOK 2 - BP2 
1. Ihsan Lana Valenza - J0403221032
2. Syifa Nursaadah  - J0403221062
3. Wildan Holik - J0403221025
4. Ibnu Aqil Mahendar - J0403221051
5. Muhammad Farhan Fahrezy - J0403221155
'''


import os
os.system("CLS")

def banner():
    import os
    os.system("cls") 
    font = """\033[0;35m

 █████╗ ██████╗  ██████╗ ████████╗███████╗██╗  ██╗    ████████╗███████╗██████╗ ██████╗  █████╗ ██╗     
██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██║ ██╔╝    ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║     
███████║██████╔╝██║   ██║   ██║   █████╗  █████╔╝        ██║   █████╗  ██████╔╝██████╔╝███████║██║     
██╔══██║██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔═██╗        ██║   ██╔══╝  ██╔══██╗██╔═══╝ ██╔══██║██║     
██║  ██║██║     ╚██████╔╝   ██║   ███████╗██║  ██╗       ██║   ███████╗██║  ██║██║     ██║  ██║███████╗
╚═╝  ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝
                                                                                                       \033[0;35m"""
    return font


class queue:
    def __init__(self):
        self.current_size = 0
        self.data = []

    def datakosong(self):
        if self.current_size == 0:
            return True
        else:
            return False

    def tambahdata(self, newdata):
        os.system("CLS")
        print("==============================")
        print("| Tambah Data Antrian Apotik |")
        print("==============================")
        print("\033[96mFormat Input : Nomor Antrian - Nama\033[0m")
        newdata = str(input("\nMasukkan Data Antrian : "))
        self.data.append(newdata)
        self.current_size = len(self.data)
        print("\nData Antrian :", newdata, "Berhasil ditambahkan")
        print("\nTekan [Enter] untuk melanjutkan")
        input()
        menu_utama()

    def panggilantrian(self):
        os.system("CLS")
        print("===============================")
        print("|       Panggil Antrian       |")
        print("===============================")
        if self.datakosong():
            print("\n\033[91mMohon maaf, Antrian kosong! Tidak ada antrian yang dapat dipanggil\033[0m")
            input("\nTekan [enter] untuk melanjutkan")
            menu_utama()
            return None
        else:
            datakeluar = self.data.pop(0)
            self.current_size = len(self.data)
            
        print("\nData Antrian : ", "Antrian Nomor" ,datakeluar, "Dipanggil")
        input("\nTekan [enter] untuk melanjutkan")
        return menu_utama()  # Menambahkan return untuk kembali ke menu utama

    def editnama(self):
        os.system("CLS")
        print("===============================")
        print("|      Edit Data Antrian      |")
        print("===============================")
        if self.datakosong():
            print("\033[91mData Antrian Kosong\033[0m")
        else:
            nomor_antrian = int(input("Masukkan Nomor Antrian yang akan diubah namanya: "))
            if nomor_antrian > 0 and nomor_antrian <= self.current_size:
                new_nama = input("Masukkan Nama Baru: ")
                self.data[nomor_antrian - 1] = f"{nomor_antrian} - {new_nama}"
                print("\nNama pada Nomor Antrian", nomor_antrian, "telah diubah menjadi", new_nama)
            else:
                print("\033[91mNomor Antrian tidak valid\033[0m")
        
        input("\nTekan [enter] untuk melanjutkan")
        menu_utama()


    def infodata(self):
        os.system("CLS")
        print("=============================")
        print("|  Informasi Data Antrian   |")
        print("=============================")
        print("\033[93mBanyak Antrian :",self.current_size)
        print("\nInformasi antrian :")
        if self.datakosong():
            print("\033[91mData Antrian Kosong\033[0m")
        else:
            print("\033[93mData antrian paling depan :", self.data[0])
            
            print("Data Antrian paling belakang :", self.data[self.current_size-1])
        print("\nTekan [enter] untuk melanjutkan")
        input()
        menu_utama()
   

    def lihatsemuadata(self):
        os.system("CLS")
        print("===============================")
        print("|     Semua Data Antrian       |")
        print("===============================")
        if self.datakosong():
            print("\033[91mData Antrian Kosong\033[0m")
        else:
            for i, data in enumerate(self.data, start=1):
                print(f"{i}. {data}")
        print("\nTekan [enter] untuk melanjutkan")
        input()
        menu_utama()

def menu_utama():
    import os
    os.system("CLS")
    print(banner())
    print("\033[94m================================\033[0m")
    print("\033[94m| Program Antrian Apotik Terpal |\033[0m")
    print("\033[94m================================\033[0m")

    print("\033[94mDaftar Layanan: \033[0m")
    print("\033[94m[1] Tambah Antrian\033[0m")
    print("\033[94m[2] Informasi Antrian\033[0m")
    print("\033[94m[3] Lihat Semua Data Antrian\033[0m")
    print("\033[94m[4] Edit Data Antrian\033[0m")
    print("\033[94m[5] Panggil Antrian\033[0m")
    print("\033[94m[0] Keluar Program\033[0m\n")
    pilihan = input("\033[96mMasukkan nomor layanan : \033[0m")
    pilihmenu(pilihan)


def pilihmenu(p):
    if p == '1':
        Q1.tambahdata("")
    elif p == '2':
        Q1.infodata()
    elif p == '3':
        Q1.lihatsemuadata()
    elif p == '4':
        Q1.editnama()
    elif p == '5':
        Q1.panggilantrian()
    elif p == '0':
        os.system("CLS")
        print("====================================")
        print("|  Anda telah keluar dari program  |")
        print("|          Terima Kasih            |")
        print("====================================")
    else:
        os.system("CLS")
        print("==========================================")
        print("|              Mohon Maaf                |")
        print("| Layanan yang anda pilih tidak tersedia |")
        print("==========================================")

Q1 = queue()
menu_utama()
