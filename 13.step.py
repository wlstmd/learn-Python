import random

# def 함수
def sum(a, b):
    result = a + b
    return result

x = sum(2, 3)
y = sum(3, 4)
print(x)
print(y)

# 매개변수가 없는 함수
def getRandomNumber():
    number = random.randint(1, 10)
    return number

print(getRandomNumber())

# 매개변수만 있는 함수
def printName(name):
    print(name)

printName("coding")

# 매개변수와 리턴값도 없는 함수
def sayHi():
    print("안녕하세요")

sayHi()