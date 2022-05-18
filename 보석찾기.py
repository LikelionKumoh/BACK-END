import random
import keyboard

mapSize=int(input("맵의 크기를 입력세요: "))
bombCount=int(input("폭탄의 갯수를 입력하세요: "))

hx=0
hy=0
map=[]
def mapSetting(mapSize, bombCount):
    global hx, hy, x_pos1, x_pos2, y_pos1,y_pos2
    for _ in range(mapSize):
        temp=["⬜" for _ in range(mapSize)]
        map.append(temp)
    map[hx][hy]="⬛️"
    x_pos1 = random.randint(1, mapSize-1)
    y_pos1 = random.randint(1, mapSize-1)
    map[x_pos1][y_pos1] = "★"
    for i in range(0, bombCount):
        x_pos2 = random.randint(1, mapSize-1)
        y_pos2 = random.randint(1, mapSize-1)
        map[x_pos2][y_pos2]="▲"
        if ((x_pos2==0 and y_pos2==0) or (x_pos1==x_pos2 and y_pos1 == y_pos2)):
            i=i-1
        
mapSetting(mapSize, bombCount)

def check_map(hx, hy):
    if (hx>mapSize or hy>mapSize):
        print("맵밖을 벗어났습니다.")
        return True
    if (hx <= -1 or hy <= -1):
        print("맵밖을 벗어났습니다.")
        return True
    if(hx==x_pos2) and (hy==y_pos2):
        print("장애물을 만났습니다.")
        return True      
    if(hx==x_pos1) and (hy==y_pos1):
        print("보물을 찾았다!")
        return True

while True:
    for i in range(mapSize):
        for j in range(mapSize):
            print(map[i][j],end="")
        print()

    dis=input("움직일 방향을 입력하세요: ")
    
    if dis=="w":
        map[hx][hy]="⬜"
        hx-=1
        map[hx][hy]="⬛️"
        if(check_map(hx, hy)):
            break
    if dis=="a":   
        map[hx][hy]="⬜"
        hy-=1
        map[hx][hy]="⬛️"
        if(check_map(hx, hy)):
            break
    if dis=="s":
        map[hx][hy]="⬜"
        hx+=1
        map[hx][hy]="⬛️"
        if(check_map(hx, hy)):
            break
        check_map(hx, hy)
    if dis=="d":  
        map[hx][hy]="⬜"
        hy+=1
        map[hx][hy]="⬛️"
        if(check_map(hx, hy)):
            break

    print("현재위치: "+ str(hx)+", "+str(hy))