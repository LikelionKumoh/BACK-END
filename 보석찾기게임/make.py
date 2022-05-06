import random
import time

mapsize=int(input("맵의 크기를 입력해주세요: "))
bombcount=int(input("폭탄의 개수를 정해 주세요: "))
map = []

for _ in range(mapsize):
    subList = ['⬜' for _ in range(mapsize)]
    map.append(subList)


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

print("================게임을 시작합니다.================")

while True:
    
    for x in range(mapsize):
        for y in range(mapsize):
            print(map[x][y], end='')
        print()

    print("1.아래로 이동")
    print("2.위로 이동")
    print("3.오른쪽으로 이동")
    print("4.왼쪽으로 이동")
    print("5.게임 종료")

    select = int(input("원하는 숫자를 입력해 주세요: "))

    if select==1:
        x = UserX+1
        y = UserY
        if x > (mapsize-1):
            x-1
            print("벗어났습니다 다시 입력해주세요.")
        elif map[x][y]=='🔺':
            print("사망하셨습니다.")
            break
        elif map[x][y]=='💠':
            print("승리하셨습니다.")
            break
        else:
            map[x][y]='🔳'
            map[UserX][UserY]='⬜'
            UserX=x
            UserY=y
            print("아래로 이동합니다.")
    elif select==2:
        x = UserX-1
        y = UserY
        if x < 0:
            x+1
            print("벗어났습니다 다시 입력해주세요.")
        elif map[x][y]=='🔺':
            print("사망하셨습니다.")
            break
        elif map[x][y]=='💠':
            print("승리하셨습니다.")
            break
        else:
            map[x][y]='🔳'
            map[UserX][UserY]='⬜'
            UserX=x
            UserY=y
            print("위로 이동합니다.")
    elif select==3:
        x = UserX
        y = UserY+1
        if y > mapsize-1:
            y-1
            print("벗어났습니다 다시 입력해주세요.")
        elif map[x][y]=='🔺':
            print("사망하셨습니다.")
            break
        elif map[x][y]=='💠':
            print("승리하셨습니다.")
            break
        else:
            map[x][y]='🔳'
            map[UserX][UserY]='⬜'
            UserX=x
            UserY=y
            print("오른쪽으로 이동합니다.")
    elif select==4:
        x = UserX
        y = UserY-1
        if y < 0:
            y+1
            print("벗어났습니다 다시 입력해주세요.")
        elif map[x][y]=='🔺':
            print("사망하셨습니다.")
            break
        elif map[x][y]=='💠':
            print("승리하셨습니다.")
            break
        else:
            map[x][y]='🔳'
            map[UserX][UserY]='⬜'
            UserX=x
            UserY=y
            print("왼쪽으로 이동합니다.")
    elif select==5:
        print("종료합니다.")
        break
    
