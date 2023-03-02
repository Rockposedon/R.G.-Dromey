n = int(input("enter the numbers : "))
b = 0
for i in range(1,n+1):
    b = i
    for j in range(2,n):
        b = i*j
    print(b)
