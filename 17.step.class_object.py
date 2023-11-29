# 클래스와 객체에 대한 개념은 각자 공부 해보고 코드를 분석 해보자 >> 중요 하기 때문에 공부를 시키는 것이다
class Monster:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f'나는 {self.name} {self.age}살 입니디.')

shark = Monster('상어', 7)
wolf = Monster('늑대', 3)

shark.say()
wolf.say()
