import random

# 맵크기 + 폭탄개수 입력받기
map = []
box = []
while True:
  item = int(input("맵 크기를 입력해주세요 : "))
  bomb = int(input("폭탄 개수를 정해주세요 : "))
  break

# 맵 생성, 출력p
# "⬜"🔳💠🔺
while True:
  for i1 in range(item):
    map.append("⬜")
  for i2 in range(item):
    box.append(map)
  for i3 in range(bomb):
    box[i3][i3] = "🔺"
  move = "🔳"
  box[0][1] = move
  box[0][2] = "💠"
  print(box)
# 말 이동하기
  print("1번 - 아래로 이동", "\n", "2번 - 위로 이동", "\n",
          "3번 - 오른쪽으로 이동", "\n", "4번 - 왼쪽으로 이동", "\n", "5번 - 게임종료")
  move = int(input("원하는 숫자를 입력해주세요: "))
  if move == 1:
    box = [move+1][move]
  elif move == 2:
    box = [move-1][move]
  elif move == 3:
    box = [move][move+1]
  elif move == 4:
    box = [move][move-1]
  else:
    break
