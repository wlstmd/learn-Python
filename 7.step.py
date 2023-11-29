# 반복문 연습 1
names = ["티모", "꼬부기", "파이리"]

for name in names:  # 반복문은 말그대로 반복하는 역할을 한다 for안에 name은 값을 저장한 변수역할 in 뒤에 names는 리스트를 의미한다
    if name == "티모":
        print(name + "는 ^모^ 입니다.")
    elif name == "꼬부기":
        print(name + "은 포켓몬입니다.")
    else:
        print(name + "은 포켓몬입니다!!")