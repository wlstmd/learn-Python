# 첫번째 별찍기 방법

# 알고리즘 문제이다 한 번 풀어보자 !
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="") # 파이썬은 end="\n"가 생략되어 print문을 하면 줄바꿈이 된다 하지만 이것을 제거하기위해 end=""를 사용했다
    print("")

# 두번째 별찍기 방법
for k in range(1, 6):
    print("*" * k)


# 거꾸로 별찍기
num = int(input("number input : "))
for i in range(1, num):
    print("*" * (num - i))

# 좌우 반전 별찍기
for i in range(1, num):
    print(" " * (num - i) + "*" * i)

# 좌우 반전 거꾸로 별찍기
for i in range(1, num):
    print(" " * (i - 1) + "*" * (num - i))
