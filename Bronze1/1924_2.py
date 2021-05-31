Month, day = map(int,input().split())
days = 0

for i in range(1,Month+1):
    if i in [2,4,6,8,9,11,13]:
        days += 31
    if i in [5,7,10,12]:
        days += 30
    if i in [3]:
        days +=28

days += day
sevendays = ["SUN","MON","TUE","WED","THU","FRI", "SAT"]

days = days % 7
print(sevendays[days])



