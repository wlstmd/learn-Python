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
