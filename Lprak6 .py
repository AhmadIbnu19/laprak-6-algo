def isian():
    jawaban = "yes"
    while jawaban.lower() == "yes":
        bulan = int(input('Masukan bulan dengan angka: '))
        tahun = int(input('Masukan tahun dengan angka: '))
        hitung_bulan(bulan, tahun)
        jawaban = input('Apakah ingin melanjutkanya? (yes/no): ')
        
def hitung_bulan(bulan, tahun):
    if bulan >= 13 or bulan <= 0:
        print('Bulan yang anda masukan tidak terdaftar di kalender')
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        print(f'Dalam bulan ke-{bulan} ada total 31 hari')
    elif bulan == 2:
        if tahun % 4 == 0:
            print(f'Dalam bulan ke-{bulan} ada total 29 hari')
        else:
            print(f'Dalam bulan ke-{bulan} ada total 28 hari')
    else:
        print(f'Dalam bulan ke-{bulan} ada total 30 hari')
isian()