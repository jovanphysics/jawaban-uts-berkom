"""Tebak Angka"""
p1 = int(input('Angka dari pemain 1: '))
for i in range(5):
    p2 = int(input('Angka dari pemain 2: '))
    if p1 == p2:
        print('Selamat, Anda pas!')
        break
    else:
        s = p2 - p1
        if s > 10:
            print('Terlalu besar')
        elif s <= 10 and s > 0:
            print('Lebih besar')
        elif s < 0 and s >= -10:
            print('Lebih rendah')
        else: 
            print('Terlalu rendah')
if p1 != p2:
    print('Maaf, Anda belum beruntung!')