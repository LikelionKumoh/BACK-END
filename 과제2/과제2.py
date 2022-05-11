import random

def printMap(mapSize):
    print(mapSize)
    for i in range(mapSize):
        for j in range(mapSize):
            print(map[i][j], end=" ")
        print('')

def checkMap(x,y):
    if(map[x][y] =='🔺'):
        print('실패!!')
        return True
    if(map[x][y] == '💠'):
        print('성공!!')
        return True

mapSize = int(input('맵의 크기를 입력하여 주세요 : '))
bombCount = int(input('폭탕 개수를 정해 주세요 : '))
global x, y
x = 0
y = 0

map = []
for _ in range(mapSize):
    sub = ['⬜' for _ in range(mapSize)]
    map.append(sub)
        
for _ in range(bombCount):
    randomRow = random.randrange(1,2000) % mapSize
    randomCol = random.randrange(1,2000) % mapSize
    map[randomRow][randomCol] = '🔺'

randomRow = random.randrange(1,2000) % mapSize
randomCol = random.randrange(1,2000) % mapSize
map[randomRow][randomCol] = '💠'
map[x][y] = '🔳'

while True:
    printMap(mapSize)
    print('1. 위로 이동'), print('2. 아래로 이동'), print('3. 오른쪽 이동'), print('4. 왼쪽 이동'), print('5. 게임 종료')
    select = int(input('원하는 숫자를 입력하여 주세요.'))
    if(select == 1 and x > 0):
        map[x][y] = '⬜'
        x -= 1
        if(checkMap(x,y)):
            break
        map[x][y] = '🔳'
        
    elif(select == 2 and x < mapSize-1):
        map[x][y] = '⬜'
        x += 1
        if(checkMap(x,y)):
            break
        map[x][y] = '🔳'
        
    elif(select == 3 and y < mapSize-1):
        map[x][y] = '⬜'
        y += 1
        if(checkMap(x,y)):
            break
        map[x][y] = '🔳'
        
    elif(select == 4 and y > 0):
        map[x][y] = '⬜'
        y -= 1
        if(checkMap(x,y)):
            break
        map[x][y] = '🔳'
        
    elif(select == 5):
        print('게임 종료')
        break
    else:
        print('다시 입력해주세요. ')
