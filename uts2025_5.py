"""Tren Berat Badan Idol K-Pop"""
# subprogram
def hitung_rerata(arr):
    jumlah = 0
    banyak = 0
    for i in arr:
        jumlah += i
        banyak += 1
    return jumlah / banyak
def hitung_tren(arr):
    # hitung panjang array
    panjang = 0
    for i in arr:
        panjang += 1
    # hitung bulan naik, bulan turun, dan bulan stabil
    bulan_naik = 0
    bulan_turun = 0
    for i in range(1, panjang):
        if arr[i] > arr[i-1]:
            bulan_naik += 1
        elif arr[i] < arr[i-1]:
            bulan_turun += 1
    # kembalikan tren
    if bulan_naik > bulan_turun:
        return 'naik'
    elif bulan_naik == bulan_turun:
        return 'stabil'
    else:
        return 'turun'
    
    

# program utama 
berat_badan = [0 for _ in range(12)]
for i in range(12):
    nilai_berat_badan = int(input(f'Input berat badan untuk bulan ke-{i+1}: '))
    berat_badan[i] = nilai_berat_badan
print(f'Tren berat badan: {hitung_tren(berat_badan)}')
print(f'Rata-rata berat badan: {hitung_rerata(berat_badan):.2f} kg')