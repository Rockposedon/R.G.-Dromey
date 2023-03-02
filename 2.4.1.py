x = int(input("enter value : "))
y = int(input("enter value : "))

def factorial(n,m):
    if n == 0:
        return 1
    else:
        return m**n / n * factorial(n - 1)
print(factorial(x,y))
