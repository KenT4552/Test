a = int(input("a : "))
b = int(input("b : "))
number = 0
summa = 0
summaF = 0
if a < b:
    for i in range(a,b+1):
        for D in range(1,i+1):
            if i % D == 0:
                summa += D

        if summaF < summa:
            summaF = summa
            number = D
        summa = 0
print(number)
print(summaF)