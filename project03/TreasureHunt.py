import random


def make_treasure_map():
    arr = [["⬜" for col in range(map_size)] for row in range(map_size)]
    arr[horse_pos['row']][horse_pos['col']] = "🔳"
    return arr

def print_treasure_map():
    for row in range(map_size):
        for col in range(map_size):
            print(treasure_map[row][col], end='')
        print()

def insert_bomb_and_treasure():
    arr = [x for x in range(1, map_size*map_size)] # [0,0]은 말의 처음 위치
    rand_arr = random.sample(arr, bomb_cnt + 1) # 폭탄 개수 + 보물 1개
    tresure = random.choice(rand_arr)

    for pos in rand_arr:
        row = pos // map_size
        col = pos % map_size
        if (pos != tresure):
            bomb_pos.append({'row' : row, 'col' : col})
            treasure_map[row][col] = "🔺"
        else:
            treasure_pos['row'] = row
            treasure_pos['col'] = col
            treasure_map[row][col] = "💠"

def move_horse(direction) :
    before_row = horse_pos['row']
    before_col = horse_pos['col']

    if direction == 1 and (before_row < map_size-1): # 아래로 이동
        horse_pos['row'] = before_row + 1
    elif direction == 2 and (before_row > 0): # 위로 이동
        horse_pos['row'] = before_row - 1
    elif direction == 3 and (before_col < map_size-1): # 오른쪽 이동
        horse_pos['col'] = before_col + 1
    elif direction == 4 and (before_col > 0): # 왼쪽 이동
        horse_pos['col'] = before_col - 1
    else:
        return -1

    treasure_map[before_row][before_col] = "⬜"
    treasure_map[horse_pos['row']][horse_pos['col']] = "🔳"

def check_catch_treasure():
    if (treasure_pos['row'] == horse_pos['row']):
        if (treasure_pos['col'] == horse_pos['col']):
            return 1
    return 0

def check_bomb_pos():
    for x in range(bomb_cnt):
        if (bomb_pos[x]['row'] == horse_pos['row']):
            if (bomb_pos[x]['col'] == horse_pos['col']):
                return 1
    return 0

def handler() :
    print("\n1.아래로 이동"
          "\n2.위로 이동"
          "\n3.오른쪽 이동"
          "\n4.왼쪽 이동"
          "\n5.게임 종료")

treasure_pos = {"row" : 0, "col" : 0}
horse_pos = {"row" : 0, "col" : 0}
bomb_pos = []
map_size = int(input("맵의 크기를 입력하여 주세요 : "))
bomb_cnt = int(input("폭탄 개수를 정해 주세요 : "))
treasure_map = make_treasure_map()
insert_bomb_and_treasure()
print_treasure_map()

print("================게임을 시작합니다.==================\n")
print_treasure_map()

while True:
    handler()
    menu = int(input("원하는 숫자를 입력하여 주세요 : "))
    if menu == 5:
        break
    elif 1 <= menu & menu <= 4:
        if move_horse(menu) == -1:
            print("이동할 수 없습니다.")
        if check_catch_treasure() == 1:
            break
        if check_bomb_pos() == 1:
            print("!!!!!!!!!!!!!펑!!!!!!!!!!!!!!")
            break
        print_treasure_map()
    else:
        print("잘못된 입력입니다.")

print("게임을 종료합니다.")