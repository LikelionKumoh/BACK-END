import random
import time

map = []
bomb = []
x = 0
y = 0
dia_x = 0
dia_y = 0
map_int = int(input("맵 크기를 입력해주세요 : "))
bomb_int = int(input("폭탄 개수를 정해주세요 : "))

# ⬜🔳💠🔺
def create(map_int, bomb_int):
    global dia_x,dia_y
    for i in range(map_int):
        box = ["⬜" for _ in range(map_int)]
        map.append(box)
        
    map[0][0] = "🔳"
  
    while(True):
        dia_x = random.randint(0,map_int-1)
        dia_y = random.randint(0,map_int-1)
        if dia_x !=0 or dia_y != 0:
            map[dia_x][dia_y] = "💠"
            break
          
    for _ in range(bomb_int):
        while(True):
            bomb_x = random.randint(0, map_int - 1)
            bomb_y = random.randint(0, map_int - 1)
            if map[bomb_x][bomb_y] ==  "⬜":
                map[bomb_x][bomb_y] ="🔺"
                bomb.append([bomb_x,bomb_y])
                break
              
def printmap(map):
    for x in range(map_int):
        for y in range(map_int):
            print(map[x][y], end="")
        print()
                  
def move(num):
    global y,x
    if num == 1:
        if y -1 >= 0 :
            map[x][y] = "⬜"
            map[x][y -1] = "🔳"
            y = y - 1
    elif num ==2:
        if y + 1 < map_int:
            map[x][y] = "⬜"
            map[x][y + 1] = "🔳"
            y = y + 1
    elif num == 3:
        if x - 1 >= 0 :
            map[x][y] = "⬜"
            map[x-1][y] = "🔳"
            x = x - 1
    elif num ==4:
        if x + 1 < map_int:
            map[x][y] = "⬜"
            map[x+1][y] = "🔳"
            x = x + 1
    elif num == 5:
        print("게임을 종료합니다. ")
        exit(0)    
        
create(map_int,bomb_int)
while True:
    printmap(map)
    print("1번 - 왼쪽으로 이동", "\n", "2번 - 오른쪽으로 이동", "\n",
          "3번 - 위로 이동", "\n", "4번 - 아래로 이동", "\n", "5번 - 게임종료")
    num = int(input("번호를 선택하세요:"))
    move(num)
    if x == dia_x and y == dia_y:
        print("보석을 찾았습니다")
        break
    if [x,y] in bomb:
        print("폭탄을 밟았습니다")
        break
