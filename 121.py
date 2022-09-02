n = int(input("Введите число : "))
count = 1

for i in range(1,n+1):
    for b in range((2*i)-1):
        if b < i:
            count = 1
            print(b+1 , end= '')
        elif b >= i:
            print(i-count , end = '')
            count += 1
    print()
