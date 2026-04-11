angka = [1,1,2,2,3,3,4,4,5,5,6,6]
hasil = []

for x in angka:
    if x not in hasil:
        hasil.append(x)
print(hasil)