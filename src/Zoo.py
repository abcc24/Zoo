class Zoo:
    def __init__(self, fences, zoo_keepers):
        self.fences = fences
        self.zoo_keepers = zoo_keepers
    
    def describe_zoo(self):
        print(f"The zookeeper is {self.zoo_keepers}, the fences are {self.fences}")
    

class Animal:
    def __init__(self, name: str, species: str, age: int, 
                 height: float, width: float, prefered_habitat: str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.prefered_habitat = prefered_habitat
        self.health = round(100*(1/age),3)
        self.animal_area = height * width

    def animal_desc(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Height: {self.height}, Width: {self.width}, Prefered habitat: {self.prefered_habitat}, Health: {self.health}")

class Fence:
    def __init__(self, area: int, temperature: float, habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animal: Animal = []

class ZooKeeper:
    def __init__(self, name: str, surname: str, id: str):
        self.name = name
        self.surname = surname
        self.id = id
        self.fence = Fence
        self.animal = Animal

    def add_animal(self, animal: Animal, fence: Fence):
        if animal not in fence.animal:
            if animal.animal_area < fence.area:
                if animal.prefered_habitat == fence.habitat:
                    fence.animal.append(animal)
                    print(f"The new animal is a {animal.species}")
                else:
                    ("No new animal")

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animal:
            fence.area += animal.animal_area
            fence.animal.remove(animal)
            print(f"The animal was removed")
 
    def feed(self, animal: Animal, fence: Fence = None):
        if animal.health < 100 and animal.animal_area < fence.area:
            animal.health = animal.health + (animal.health * 1.01)
            animal.animal_area = animal.animal_area + (animal.animal_area * 1.02)
            print(f"The animal is eating! Health: {animal.health} Animal area {animal.animal_area}")
        elif animal.health == 100 and animal.animal_area < fence.area:
            print("The animal is healty")
        elif animal.health <= 100 and animal.animal_area > fence.area:
            print("The animal is too big")

    def clean(self, fence: Fence, animal: Animal = None):
        new_area = fence.area - animal.animal_area
        if new_area > 0:
            for animal in fence.animal:      
                clean = new_area / animal.animal_area           
                for animal in fence.animal:
                    fence.animal.remove(animal)
                    print(f"The cleaning time is {clean}")