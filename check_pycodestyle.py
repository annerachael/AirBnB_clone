class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        """
        This method makes the animal produce its characteristic sound.
        """
        print(self.sound)


class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog", "Woof")
        self.name = name

    def greet(self):
        """
        This method makes the dog greet by barking.
        """
        print("Hello, I'm {} the {}!".format(self.name, self.species))


if __name__ == "__main__":
    # Example usage
    my_dog = Dog("Buddy")
    my_dog.greet()
    my_dog.make_sound()
