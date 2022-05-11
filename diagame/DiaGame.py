import time
import random

mapsize = int(input("맵의 크기를 입력해 주세요: "))
bombcount = int(input("폭탄의 갯수를 입력해 주세요"))
userX = 0
userY = 0
dia_x = 0
dia_y = 0
bomb = []
map =[]
def createmap(mapsize,bombcount):
    #맵만들기
    global dia_x,dia_y
    for _  in range(mapsize):
        sublist = ["⬜" for _ in range(mapsize)]
        map.append(sublist)

    map[0][0] = "🔳"
    #다이아 넣기
    while(True):
        dia_x = random.randint(0,mapsize-1)
        dia_y = random.randint(0,mapsize-1)
        if dia_x !=0 or dia_y != 0:
            map[dia_x][dia_y] = "💠"
            break

    #폭탄넣기
    for _ in range(bombcount):
        while(True):
            bomb_x = random.randint(0, mapsize - 1)
            bomb_y = random.randint(0, mapsize - 1)
            if map[bomb_x][bomb_y] ==  "⬜":
                map[bomb_x][bomb_y] ="🔺"
                bomb.append([bomb_x,bomb_y])
                break


def printmap(map):
    for x in range(mapsize):
        for y in range(mapsize):
            print(map[x][y], end="")
        print()

def movelocate(num):
    #좌
    global userY,userX
    if num == 1:
        if userY -1 >= 0 :
            map[userX][userY] = "⬜"
            map[userX][userY -1] = "🔳"
            userY = userY - 1
    #우
    elif num ==2:
        if userY + 1 < mapsize:
            map[userX][userY] = "⬜"
            map[userX][userY + 1] = "🔳"
            userY = userY + 1
    elif num == 3:
        if userX - 1 >= 0 :
            map[userX][userY] = "⬜"
            map[userX-1][userY] = "🔳"
            userX = userX - 1
    #하
    elif num ==4:
        if userX + 1 < mapsize:
            map[userX][userY] = "⬜"
            map[userX+1][userY] = "🔳"
            userX = userX + 1

    elif num == 5:
        print("게임을 종료합니다. ")
        exit(0)




createmap(mapsize,bombcount)
while(True):
    printmap(map)
    print("1. 좌 이동")
    print("2. 우 이동")
    print("3. 상 이동")
    print("4. 하 이동")
    print("5. 게임 종료")
    num = int(input("번호를 선택하세요:"))
    movelocate(num)
    if userX == dia_x and userY == dia_y:
        print("보석을 찾았습니다!")
        break
    if [userX,userY] in bomb:
        print("폭탄입니다!!!")
        break