import copy
import os
import time
import random
from collections import deque

# 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# ■ ★ □ ※


def init_map(map_size, bomb):
    field = [["■"] * map_size for _ in range(map_size)]
    place_object = list(range(map_size ** 2))

    field[0][0] = "□"
    place_object.remove(0)

    for _ in range(bomb):
        num = random.choice(place_object)
        field[num // map_size][num % map_size] = "※"
        place_object.remove(num)

    num = random.choice(place_object)
    field[num // map_size][num % map_size] = "★"
    return field


def display(field):
    os.system('cls')
    for i in field:
        print(*i)


def auto_play(field, x, y):
    def find(field, x, y):
        st = [x, y, []]
        visit = [[False] * len(field) for _ in range(len(field))]

        queue = deque([st])
        visit[st[1]][st[0]] = True

        while queue:
            x, y, root_arr = queue.popleft()
            for i in range(4):
                v_x = x + dx[i]
                v_y = y + dy[i]

                if not(0 <= v_x < len(field)) or not(0 <= v_y < len(field)): continue
                if visit[v_y][v_x]: continue

                visit[v_y][v_x] = True

                if (now := field[v_y][v_x]) == '★':
                    root_arr.append(i)
                    return root_arr

                elif now == '■':
                    queue.append([v_x, v_y, copy.copy(root_arr) + [i]])

    roots = find(field, x, y)
    for i in roots:
        display(field)
        time.sleep(1)
        if i == 0:  # right
            field[y][x], field[y][x + 1] = field[y][x + 1], field[y][x]
            x += 1
        elif i == 1:  # left
            field[y][x], field[y][x - 1] = field[y][x - 1], field[y][x]
            x -= 1
        elif i == 2:  # down
            field[y][x], field[y + 1][x] = field[y + 1][x], field[y][x]
            y += 1
        else:  # up
            field[y][x], field[y - 1][x] = field[y - 1][x], field[y][x]
            y -= 1


def select():
    print("1. Move Top")
    print("2. Move Down")
    print("3. Move Right")
    print("4. Move Left")
    print("5. Auto play")
    print("6. Exit")
    choice = int(input())
    return choice


map_size = int(input("Input map_size : "))
bomb = int(input("Input bomb cnts : "))
field = init_map(map_size, bomb)

user_x = user_y = 0

while True:
    display(field)
    choice = select()
    tmp_pos = (user_x, user_y)
    if choice == 6:
        print("Game end!")
        break
    elif choice == 1: user_y -= 1
    elif choice == 2: user_y += 1
    elif choice == 3: user_x += 1
    elif choice == 4: user_x -= 1
    elif choice == 5:
        auto_play(field, user_x, user_y)
        break
    else: print("Input Error!")

    if (not (0 <= user_x < map_size)) or (not (0 <= user_y < map_size)):
        user_x, user_y = tmp_pos
        print("Can't Move!")
    elif (now := field[user_y][user_x]) == '★':
        print("Game Clear!")
        break
    elif now == '※':
        print("Your Dead...")
        break
    else:
        field[tmp_pos[1]][tmp_pos[0]] = "■"
        field[user_y][user_x] = "□"