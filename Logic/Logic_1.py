

cnt = 1  # cnt 변수 초기화

for i in range(0, 9):
    if cnt < 9 and i < 5:
        for j in range(0, 4 - i):
            print(' ', end='')  # 띄어쓰기 출력
    else:
        for j in range(0, i - 4):
            print(' ', end='')  # 띄어쓰기 출력

    for z in range(0, cnt):
        print('*', end='')  # 별표 출력
    print()  # 줄 바꿈

    if cnt < 9 and i < 5:
        cnt += 2
    else:
        cnt -= 2


for x in range(0,5):
    for z in range(0,4 - x):
        print('0',end='')
    for j in range(0,(2 * x) +1):
        print('*',end='')
    print()  # 줄 바꿈    

print()  # 줄 바꿈    
for x in range(0,5):
    for z in range(0,x):
        print('0',end='')
    for j in range(0,9-(x * 2)):
        print('*',end='')
    print()  # 줄 바꿈    