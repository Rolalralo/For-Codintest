A,B,V = map(int,input().split())

up_height = 0
i = 0
while True:
    up_height += A
    i +=1
    if up_height >= V:
        print(i)
        break
    up_height -= B



        
    

