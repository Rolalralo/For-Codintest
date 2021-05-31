little_boys = []
sum_little = 0
for i in range(9):
    A = int(input())
    little_boys.append(A)

total = sum(little_boys)

while True:
    for i in little_boys:
        sum_little += i 
        if sum_little > 100:
            break

print(sum_little)


