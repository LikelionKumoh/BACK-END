import random
import time

lunch = ["냉면", "자장면", "우동", "돈까스"]
while True :
    item = input("음식을 추가 해주세요(종료(q)) : ")
    if (item == 'q'): break
    lunch.append(item)
    print(lunch)

set_lunch = set(lunch)
while True:
    item = input("삭제할 음식을 입력해주세요(종료q) : ")
    if(item == 'q'): break
    set_lunch -= set(item)
    print(set_lunch)

print(set_lunch, "중에서 선택합니다")
for x in range(5, 0, -1):
    time.sleep(1)
    print(x)
print(random.choice(list(set_lunch)))