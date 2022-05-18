import random
map =[]
box=[]

while True:
  for i1 in range(15):
    map.append(i1)
  for i2 in range(15):
    box.append(map)
  for i3 in range(5):
    r = random.randrange(0,15)
    box[r][r] = "🔺"
  result = ''.join(s for s in box) + '\n'
  
  print(result)
  break