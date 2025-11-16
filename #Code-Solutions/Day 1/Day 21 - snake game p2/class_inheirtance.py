class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breate(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()          ## Not required, optional


    def breate(self):
        super().breate()
        print("doing this under water")


    def swim(self):
        print("Moving in water.")

nemo = Fish()
nemo.breate()
