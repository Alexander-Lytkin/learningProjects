class Animal:
    def __init__(self, name):
        self._name = name


class Dog(Animal):
    def run(self):
        print(f"Dog {self._name} runs")


class Cat(Animal):
    def run(self):
        print(f"Cat {self._name} runs")


animals = [Dog("Шарик"), Cat("Vas'ka"), Dog("Кубик"), Cat("пяточок")]

for animal in animals:
    animal.run()
