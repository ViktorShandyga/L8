class Pet:
    def __init__(self, name, species="cat"):
        self.name = name
        self.species = species
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.health = 100

    def feed(self):
        if self.hunger > 20:
            self.hunger -= 20
            self.happiness += 5
            print(f"{self.name} поїв(ла) і виглядає задоволеним.")
        else:
            print(f"{self.name} не голодний(а).")

    def play(self):
        if self.energy > 20:
            self.happiness += 10
            self.energy -= 15
            self.hunger += 10
            print(f"{self.name} грається і веселиться!")
        else:
            print(f"{self.name} занадто втомлений(а), щоб гратися.")

    def sleep(self):
        if self.energy < 80:
            self.energy += 30
            self.hunger += 10
            print(f"{self.name} заснув(ла) і відпочиває.")
        else:
            print(f"{self.name} не хоче спати зараз.")

    def check_status(self):
        print(f"Ім'я: {self.name}")
        print(f"Вид: {self.species}")
        print(f"Голод: {self.hunger}")
        print(f"Енергія: {self.energy}")
        print(f"Задоволення: {self.happiness}")
        print(f"Здоров'я: {self.health}")

    def take_to_vet(self):
        if self.health < 80:
            self.health = 100
            self.happiness -= 10
            print(f"{self.name} відвідав(ла) ветеринара і почувається краще.")
        else:
            print(f"{self.name} здоровий(а) і не потребує лікаря.")

my_pet = Pet(name="Мурчик", species="котик")
my_pet.check_status()
my_pet.feed()
my_pet.play()
my_pet.sleep()
my_pet.take_to_vet()
my_pet.check_status()