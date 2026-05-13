a = 0
b = 1
c = 10

print(a)
print(b)

for i in range(3, c + 1):
    d = a + b
    print(d)
    a = b
    b = d
