import random #함수 및 키보드 입력 사용
import time
import keyboard

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

        if x!=0 or y!=0:
            map[x][y]='🔺'
            break
while True:
    x=random.randrange(0,mapsize-1)
    y=random.randrange(0,mapsize-1)
    if map[x][y]!='🔳' and map[x][y]!='🔺':
        map[x][y]='💠'
        break
def go_key():
    if keyboard.read_key() == "down":
        return 1
    elif keyboard.read_key() == "up":
        return 2
    elif keyboard.read_key() == "right":
        return 3
    elif keyboard.read_key() == "left":
        return 4
    elif keyboard.read_key() == "esc":
        return 5
def move():
    global UserX, UserY, play
    print("원하는 방향을 입력하세요(ESC를 누르면 종료)")
    select = go_key()

    if select==1:
        x = UserX+1
        y = UserY
        if x > (mapsize-1):
            x-1
            print("벗어났습니다 다시 입력해주세요.")
            time.sleep(1)
        elif map[x][y]=='🔺':
            print("사망하셨습니다.")
            play=False
        elif map[x][y]=='💠':
            print("승리하셨습니다.")
            play=False
        else:
            map[x][y]='🔳'
            map[UserX][UserY]='⬜'
            UserX=x
            UserY=y
            print("아래로 이동합니다.")
            time.sleep(1)
    elif select==2:
        x = UserX-1
        y = UserY
        if x < 0:
            x+1
            print("벗어났습니다 다시 입력해주세요.")
            time.sleep(1)
        elif map[x][y]=='🔺':
            print("사망하셨습니다.")
            play=False
        elif map[x][y]=='💠':
            print("승리하셨습니다.")
            play=False
        else:
            map[x][y]='🔳'
            map[UserX][UserY]='⬜'
            UserX=x
            UserY=y
            print("위로 이동합니다.")
            time.sleep(1)
    elif select==3:
        x = UserX
        y = UserY+1
        if y > mapsize-1:
            y-1
            print("벗어났습니다 다시 입력해주세요.")
            time.sleep(1)
        elif map[x][y]=='🔺':
            print("사망하셨습니다.")
            play=False
        elif map[x][y]=='💠':
            print("승리하셨습니다.")
            play=False
        else:
            map[x][y]='🔳'
            map[UserX][UserY]='⬜'
            UserX=x
            UserY=y
            print("오른쪽으로 이동합니다.")
            time.sleep(1)
    elif select==4:
        x = UserX
        y = UserY-1
        if y < 0:
            y+1
            print("벗어났습니다 다시 입력해주세요.")
            time.sleep(1)
        elif map[x][y]=='🔺':
            print("사망하셨습니다.")
            play=False
        elif map[x][y]=='💠':
            print("승리하셨습니다.")
            play=False
        else:
            map[x][y]='🔳'
            map[UserX][UserY]='⬜'
            UserX=x
            UserY=y
            print("왼쪽으로 이동합니다.")
            time.sleep(1)
    elif select==5:
        print("종료합니다.")
        play=False

print("================게임을 시작합니다.================")
play=True
while play:
    
    for x in range(mapsize):
        for y in range(mapsize):
            print(map[x][y], end='')
        print()

    print("1.아래로 이동")
    print("2.위로 이동")
    print("3.오른쪽으로 이동")
    print("4.왼쪽으로 이동")
    print("5.게임 종료")

    move()

    
    
