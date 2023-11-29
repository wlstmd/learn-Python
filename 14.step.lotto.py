import random

lotto_num = [] # 빈 로또 번호 리스트 생성

def getRandomNumber():
    number = random.randint(1, 45)
    return number

count = 0
# 무한 반복
while count < 6:
    random_number = getRandomNumber()
    if random_number not in lotto_num: # 로또번호 리스트 안에 뽑은 로또번호가 없다면 뽑은 로또번호를 추가한다.
        lotto_num.append(random_number)
        count += 1
print(lotto_num)