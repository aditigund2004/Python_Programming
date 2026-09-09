for i in range(1, 4):
    for j in range(1, i + 1):
        print("*", end="")
    print()


for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end="")




for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")



for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end="")
    print()




for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(j, end=" ")




for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(j, end=" ")



count = 0

for i in range(3):
    for j in range(2):
        count += 1

print(count)




sum = 0

for i in range(1, 4):
    for j in range(1, 4):
        sum += i

print(sum)
