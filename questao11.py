lista = []

for num in range(5):
    lista.append(int(input("numero ->")))

for num in lista:
    if num % 2 == 1:
        print(num)