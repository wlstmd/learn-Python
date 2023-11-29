# 파이썬에서의 연산

# 숫자 연산
x = 5
y = 2

print(x + y)  # 더하기
print(x - y)  # 빼기
print(x * y)  # 곱하기
print(x / y)  # 나누기
print(x // y)  # 몫
print(x % y)  # 나머지
print(x ** y) # 제곱

# 문자 연산
text1 = "#오늘은"
text2 = "#월요일"
text3 = "#월요병"

total_text = text1 + "\n" + text2 + "\n" + text3*3
print(total_text)
# "\n"은 줄바꿈 코드를 나타낸다.

# 비교 연산
a = 1
b = 2
print(a > b)  # a가 b보다 크다 참 아니라면 거짓
print(a < b)  # a가 b보다 작다면 참 아니라면 거짓
print(a >= b)  # a가 b보다 크거나 같다면 참 아니면 거짓
print(a <= b)  # a가 b보다 작거나 같다면 참 아니면 거짓
print(a == b)  # a랑 b가 같다면 참 아니면 거짓
print(a != b)  # a랑 b랑 다르다면 참 아니면 거짓

#논리 연산
# 논리연산에서는 1을 참 나머지숫자를 거짓으로 처리한다 대표적으로는 0이 거짓이다
c = 1
d = 0
print(c and d)  # and연산자는 둘다 참이어야 참이다 이코드는 1 : 0 이므로 거짓이다
print(c or b)  # or연산자는 둘 중 어느 하나라도 참이라면 참을 출력한다 / 0 : 0 이라면 거짓을 출력
print(not c)  # not연산자는 1을 0으로 0을 1으로 반대로 변환해주는 역할을 한다
