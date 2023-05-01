def fibonacci(n):
    n+=1

    n1, n2 = 0, 1
    count = 0

    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


num = int(input("numero ->"))
while(num % 2 == 0):
    num = int(input("numero ->"))

fibonacci(num)