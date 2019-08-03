class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    # Python does not like empty class so put pass
    pass


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
