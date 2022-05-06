import random
import time

mapsize=int(input("맵의 크기를 입력해주세요: "))
bombcount=int(input("폭탄의 개수를 정해 주세요: "))
map = []

for _ in range(mapsize):
    subList = ['⬜' for _ in range(mapsize)]
    map.append(subList)

print("================게임을 시작합니다.================")

UserX=0
UserY=0
map[UserX][UserY]='🔳'
for _ in range(bombcount):
    while True:
        x=random.randrange(0,mapsize-1)
        y=random.randrange(0,mapsize-1)

        if map[x]!=0 or map[y]!=0:
            map[x][y]='🔺'
            break
while True:
    x=random.randrange(0,mapsize-1)
    y=random.randrange(0,mapsize-1)
    if map[x][y]!='🔳' and map[x][y]!='🔺':
        map[x][y]='💠'
        break



for x in range(mapsize):
    for y in range(mapsize):
        print(map[x][y], end='')
    print()

print("1.아래로 이동")
print("2.위로 이동")
print("3.오른쪽으로 이동")
print("4.왼쪽으로 이동")
print("5.게임 종료")
select = input("원하는 숫자를 입력하여 주세요: ")

if select==1:
    UserX = UserX+1
    UserY = UserY
