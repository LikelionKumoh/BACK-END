import random
import time

MapSize = int(input("맵 크기를 설정하세요: "))
Bomb = int(input("폭탄 개수를 설정하세요: "))

MapList = []

for _ in range(MapSize):
    SubList = []
    for _ in range(MapSize):
        SubList.append("⬜")

    MapList.append(SubList)

MapList[0][0] = "🔳"

UserX = 0
UserY = 0

result = 0

def down():
    global UserX, UserY
    nX = UserX+1
    nY = UserY
    if (nX < MapSize and nX >= 0) and MapList[nX][nY] == "⬜":
        MapList[nX][nY] = "🔳"
        MapList[UserX][UserY] = "⬜"
        UserX = nX
        result = 0
        return result   
    elif MapList[nX][nY] == "💠":
        result = 1
        return result    
    else:
        result = 2
        return result

def up():
    global UserX, UserY
    nX = UserX-1
    nY = UserY
    if (nX < MapSize and nX >= 0) and MapList[nX][nY] == "⬜":
        MapList[nX][nY] = "🔳"
        MapList[UserX][UserY] = "⬜"
        UserX = nX
        result = 0
        return result   
    elif MapList[nX][nY] == "💠":
        result = 1
        return result 
    else:
        result = 2
        return result

def right():
    global UserX, UserY
    nX = UserX
    nY = UserY+1
    if (nX < MapSize and nX >= 0) and MapList[nX][nY] == "⬜":
        MapList[nX][nY] = "🔳"
        MapList[UserX][UserY] = "⬜"
        UserY = nY
        result = 0
        return result   
    elif MapList[nX][nY] == "💠":
        result = 1
        return result 
    else:
        result = 2
        return result

def left():
    global UserX, UserY
    nX = UserX
    nY = UserY-1
    if (nX < MapSize and nX >= 0) and MapList[nX][nY] == "⬜":
        MapList[nX][nY] = "🔳"
        MapList[UserX][UserY] = "⬜"
        UserY = nY
        result = 0
        return result   
    elif (MapList[nX][nY] == "💠"):
        result = 1
        return result 
    else:
        result = 2
        return result

while True:
    x = random.randint(0, MapSize-1)
    y = random.randint(0, MapSize-1)

    if x != 0 or y != 0:
        MapList[x][y] = "💠"
        break

for i in range(Bomb):
    while True:
        x = random.randint(0, MapSize-1)
        y = random.randint(0, MapSize-1)
        if( x != 0 or y != 0 )and MapList[x][y] != '💠':
            MapList[x][y] = "🔺"
            break


print(" ")
print("============ 게임을 시작합니다. ============")
while True:
    for i in range(MapSize):
        for j in range(MapSize):
            print(MapList[i][j], end=' ')
        print()

    print(" ")
    print("1. 아래로 이동") 
    print("2. 위로 이동")
    print("3. 오른쪽으로 이동")
    print("4. 왼쪽으로 이동")
    print("5. 게임 종료")
    
    Num = int(input("\n원하는 숫자를 입력하여 주세요: "))
    print(" ")

    time.sleep(0.5)
    if Num==1:
        if down()==0:
            print("아래로 이동합니다.\n")   
        elif down()==1:
            print("축하합니다. 보석을 찾았습니다.")  
            break
        else:
            print("잘못된 위치로 이동하셨습니다.\n게임을 종료합니다.")
            break
    elif Num==2:
        if up()==0:
            print("위로 이동합니다.\n")
        elif up()==1:
            print("축하합니다. 보석을 찾았습니다.")
            break
        else: 
            print("잘못된 위치로 이동하셨습니다.\n게임을 종료합니다.")
            break
    elif Num == 3:
        if right()==0:
            print("오른쪽으로 이동합니다.\n")
        elif right()==1:
            print("축하합니다. 보석을 찾았습니다.")
            break
        else:
            print("잘못된 위치로 이동하셨습니다.\n게임을 종료합니다.")
            break
    elif Num == 4:
        if left()==0:
            print("왼쪽으로 이동합니다.\n")  
        elif left()==1:
            print("축하합니다. 보석을 찾으셨습니다.")
            break
        else:
            print("잘못된 위치로 이동하셨습니다.\n게임을 종료합니다.")
            break
    elif(Num == 5):
        print("게임을 종료합니다.\n")
        break
    else:
        print("1~5까지 숫자만 입력하세요.\n")


   
