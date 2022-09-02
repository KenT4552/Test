n = int(input())
for i in range(1,n+1):
    otvet = str(i)
    for D in range(1,i+1):
        if i % D == 0:
            otvet += '+'
    print(otvet)