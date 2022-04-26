import time
import random

lunch=["김밥","라면","잔치국수","떡볶이"]

while True:
    print(lunch)
    item= input("추가하고 싶은 메뉴를 입력하세요(없을 시 q 입력):")
    if (item=="q"):
        break
    else:
        lunch.append(item)
print(lunch)
set_lunch=set(lunch)

while True:
    print(set_lunch)
    item = input("빼고 싶은 메뉴를 입력하세요(없을 시 q 입력):")
    if (item=="q"):
        break
    else:
        set_lunch=set_lunch-set([item])

print(set_lunch,"중 에서 5초 후 오늘의 점심 메뉴를 무작위로 골라드립니다")
for x in range(5,0,-1):
    print(x)
    time.sleep(1)
print(random.choice(list(set_lunch)))
    