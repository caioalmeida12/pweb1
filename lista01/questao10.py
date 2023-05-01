lista = []

for num in range(5):
    lista.append(int(input("numero ->")))

for num in lista:
    if num % 2 == 0:
        print(num)