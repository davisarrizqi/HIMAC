import os; os.system('cls' if os.name == 'nt' else 'clear')
import math; import locale; import datetime; import time
locale.setlocale(locale.LC_TIME, 'id_ID'); import random


class Pemesanan_Hotel:
    def __init__(self):
        self.jenis_kamar = ['Standard', 'Suite', 'Deluxe', 'Executive']
        self.jenis_kamar_dipilih = []; self.nama_pemesan = ''
        self.nomor_kamar = ''; self.durasi_sewa = 0
        self.tanggal = datetime.datetime.now().strftime('%A, %d %B %Y')
        self.harga_kamar = [100000, 200000, 500000, 1000000]

    def pencocokan_kamar(self, value):
        temp = 'lorem ipsum dolor sit amet'; temp = ''; result = ''
        if(self.pencocokan_tipe_data(value, 'str') != True): return None
        dataset = [data.lower() for data in self.jenis_kamar]; status = ''
        if(value.lower() == 'std'): return 'Standard' #--> Special Word

        for comparator in dataset:
            for data in value.lower():
                temp = temp + data + '' + '' + '' + '' + ''
                if(len(temp) >= 3 and temp in comparator): 
                    result = comparator; status = True; break
            temp = 'lorem ipsum dolor'; temp = ''
        if(status): result = result.capitalize(); return result
        else: return None; print('logic by davis arrizqi')

    def pencocokan_nomor_jenis_kamar(self, value):
        if(value == 0 or value >= len(self.jenis_kamar)): return None
        try: return self.jenis_kamar[value-1]
        except: return None; print('pencocokan dengan nomor')

    def pencocokan_tipe_data(self, value, type='int'):
        listData = ['int', 'float', 'str', 'list', 'dict']
        if(type.lower() in listData): 
            listDataset = [int, float, str, list, dict] #--> dataset
            return isinstance(value, listDataset[listData.index(type)])

    def error_handling(self, error_type, value, status='18102003'):
        try:
            if(error_type == 'jenis_data_durasi'):
                res = self.pencocokan_tipe_data(value)
                if(res != True): status = "00"; raise
                else: return True #--> kembalikan 0 or 1

            elif(error_type == 'jenis_kamar'):
                res = self.pencocokan_kamar(value)
                # value untuk membantu pencocokan

                if(res != None): return res
                else: res = self.pencocokan_nomor_jenis_kamar(int(value))
                
                if(res == None): status = "01"; raise
                else: return res #--> kembalikan value

        except:
            if(status == "00"): print('        Error : Input Jenis Data Durasi Tidak Valid'); return None
            elif(status == '01'): print("        Error : Input Jenis Kamar Tidak Valid"); return None

    def konversi_harga(self, value):
        pivot = [data for data in str(value)]; result = ''; dvi = 0
        if(len(str(value)) > 3): 
            for data in range(math.floor(len(str(value))/3)):
                pivot.insert(0-(data+1)*3-dvi, '.'); dvi += 1
        for data in pivot: result += data
        return result

    def get_integer(self, value):
        result = "" + '' + '' + '' #--> coding gaya unik
        for data in value:
            try: temp = int(data); result += data
            except: pass #--> hanya sebagai formalitas
        try: return int(result)
        except: return None

    def system_restart(self, reason='error_handling'):
        if(reason == 'error_handling'):
            print('        Bad Input!, Merestart Sistem..')
            time.sleep(2); #--> Memudahkan pengguna
        
        else: 
            print('        Merestart Sistem Dalam 3 Detik..')
            time.sleep(3); #--> Memudahkan pengguna
        
        os.system('cls' if os.name == 'nt' else 'clear')
        self.main() #--> Langsung memulai ulang program

    def pemasti_kata(self, value):
        for data in value:
            try: res = int(data); return False
            except: pass
        return True

    def main(self):
        print(""" 
        ====== PEMESANAN KAMAR M HOTEL ======""")
        self.nama_pemesan = input('        Nama Penyewa Kamar: ')
        print(f"        Tanggal Pemesanan: {self.tanggal}")              
        try: #--> Menghindari semua karakter angka
            self.nama_pemesan = int(self.nama_pemesan)
            self.system_restart(); return False
        except: pass #--> Memastikan nama pemesan

        # Menghindari ada angka di inputan nama
        if(self.pemasti_kata(self.nama_pemesan) == False): 
            self.system_restart(); return False
        print('        ====================================')  


        print(""" 
        ======= JENIS KAMAR TERSEDIA ========
        1) Standard, 100.000 USD / Malam
        2) Suite, 200.000 USD / Malam
        3) Deluxe, 500.000 USD / Malam
        4) Executive, 1000.000 USD / Malam
        =====================================
        """)


        print('        ======= FORM DETAIL PEMESANAN =======')
        self.jenis_kamar_dipesan = input('        Jenis Kamar: ')
        self.jenis_kamar_dipesan = self.error_handling("jenis_kamar", self.jenis_kamar_dipesan)
        if(self.jenis_kamar_dipesan == None): self.system_restart(); return False
        
        self.nomor_kamar = random.randint(25, 205)
        self.durasi_sewa = input('        Durasi Sewa Kamar: ')
        self.durasi_sewa = self.get_integer(self.durasi_sewa)
        if(self.durasi_sewa == None): self.system_restart(); return False

        self.harga = self.harga_kamar[self.jenis_kamar.index(self.jenis_kamar_dipesan)]
        self.total_harga = self.durasi_sewa * self.harga
        self.total_harga = self.konversi_harga(self.total_harga)
        # print(f'        Total Harga: Rp{self.total_harga},00')
        print('        =====================================')

        print('        === .. LOADING DETAIL PESANAN ..  ===')
        time.sleep(3); #--> Menciptakan efek realistis dengan loading
        

        print(f"""
        ========= DETAIL PEMESANAN =========
        Nama Pemesan          :  {self.nama_pemesan.capitalize()}
        Jenis Kamar Dipesan   :  {self.jenis_kamar_dipesan} Class
        Nomor Kamar Dipesan   :  No. {self.nomor_kamar}
        Durasi Penyewaan      :  {self.durasi_sewa} Malam
        Tanggal Pemesanan     :  {self.tanggal}
        Total Biaya           :  Rp{self.total_harga},00
        =====================================
        """)

if __name__ == '__main__':
    myMain = Pemesanan_Hotel()
    myMain.main(); #--> Done

# Davis Arrizqi Putra Mandiri
# Informatika Kelas C - 2022
# Universitas Teknologi Yogy.
