# 첫번째 별찍기 방법
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
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
