N = int(input())

q_5 = N // 5
q_3 = 0

R_5 = N%5

while(q_5 >= 0):
    if (R_5 % 3 == 0):
        q_3 = R_5 // 3
        R_5 = R_5 % 3
        break
    R_5 = R_5 + 5
    q_5 = q_5 - 1

print((R_5 == 0) and (q_5 + q_3) or -1)

