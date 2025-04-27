class Animal():
    def __init__(self,name,speices):
        self.name = name
        self.speices = speices

    def speak(slef):
        return "Some sound"
    
class Dog(Animal):
    def __init__(self, name, speices):
        super().__init__(name,speices)
    def speak(self):
        return "Bark"
class Cat(Animal):
    def __init__(self, name, speices):
        super().__init__(name, speices)
    def speak(self):
        return "Meow"
class Zoo():
    def __init__(self,animals):
        self.animals = animals
    def make_all_speak(self):
        for animal in self.animals:
            print(f'''{animal.speices} ({animal.name}): {animal.speak()} ''')


if __name__ == "__main__":
    dog = Dog("Buddy","Dog")
    cat = Cat("Mittens","Cat")
    zoo = Zoo([dog,cat])

    zoo.make_all_speak()


        
    
        