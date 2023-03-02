x = list(map(int, input("enter the values : ").split()))
r = 0
for i in x :
    r += 1/i
    print(r,"\n")
print(r)
r = r /4
print(r)
harmonic_mean = 1/r
print(harmonic_mean)