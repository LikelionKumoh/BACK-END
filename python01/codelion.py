import random

print(random.choice(["된찌", "피자", "제육볶음"]))

for x in range(30):
    print(random.choice(["된찌", "피자", "제육볶음"]))

lunch = random.choice(["된찌", "피자", "제육볶음"])
dinner = random.choice(["김밥", "쫄면", "돈까스"])
print(lunch)

# dictionary
information = {"고향": "대구", "이름": "은빈", "나이": 23}
print(information)
print(information.get("고향"))
information["나이"] = 21
print(information.get("나이"))
print(len(information))
#information.clear()
print(information)

# list
foods = ["냉면", "돈까스", "치킨", "피자"]
print(foods)
print(foods[2])
foods.append("김밥")
print(foods)
del foods[0]
print(foods)

for x in range(30):
    print(x)

for x in foods:
    print(x)

for x, y in information.items():
    print(x)
    print(y)

for x, y in information.items():
    if type(y) is int:
        print(x + ": " + str(y))
    else:
        print(x + ": " + y)

# 집합
foods = ["냉면", "돈까스", "치킨", "피자"]
foods_set1 = set(foods)
print(foods_set1)

menu1 = set(["된장찌개", "피자", "떡국"])
menu2 = set(["된장찌개", "치킨", "냉면"])
menu3 = menu1 | menu2
print("menu3 :",  menu3)
menu4 = menu1 & menu2
print("menu4 :", menu4)
memu5 = menu1 - menu2
print("menu5 :", memu5)

food = random.choice(["냉면", "돈까스", "치킨", "피자"])
if (food == "냉면"):
    print("곱빼기 주세요")
else:
    print("걍 주세요")
