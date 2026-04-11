list_nama = []
print("Ketik selesai untuk berhenti \n")
while True:
    nama = input("input Name: ")
    if nama.lower() == 'selesai':
        break
    list_nama.append(nama)
if len(list_nama) > 0:
    reverse_join = " ".join(list_nama[::-1])
    print(f"{reverse_join}")
else:
    print("list kosong")