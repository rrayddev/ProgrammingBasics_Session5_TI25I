list_angka = []
for i in range(3):
    input_user = input("Input number: ")
angka = int(input_user)
list_angka.append(angka)
terbesar = max(list_angka)
print(f"The Biggest Number is {terbesar}")
