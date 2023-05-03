lista = []

for num in range(5):
    lista.append(int(input("numero ->")))

if int(input("numero para checar se está na lista->")) in lista:
    print("numero está na lista")
else:
    print("numero não está na lista")