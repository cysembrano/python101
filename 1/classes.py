class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def move():
        print("move")

    def draw(self):
        print("draw")


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


point1 = Point(10, 20)
point1.x = 10
point1.y = "20"
point1.move()
print(point1.x)
point1.draw()

point2 = Point(1, 2)
point2.x = 1
print(point2.x)


person = Person("Cyrus")
person.talk()