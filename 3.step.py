# 입력방식과 처리

# 첫번째 방법
x = input("첫번째 숫자를 입력해주세요 >>> ")
y = input("두번째 숫자를 입력해주세요 >>> ")

print(int(x) * int(y))

# 두번째 방법
a = int(input("첫번째 숫자를 입력해주세요. >>> "))
b = int(input("두번째 숫자를 입력해주세요. >>> "))

print(a * b)

# 태어난 연도를 입력받고 나이계산해서 출력하기
year = int(input("태어난 연도를 입력해주세요 >>> "))
age = 2023 - year + 1

print(str(age) + "살 입니다.")