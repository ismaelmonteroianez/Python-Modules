class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth: float) -> None:
        self.name = name
        self._height = height
        self._age = age
        self.growth = growth
        self._stats = self.Statistics()

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")
        self._stats._show_count += 1

    def advance_age(self) -> None:
        self._age += 1
        self._stats._age_count += 1

    def grow(self) -> None:
        self._height = self._height + self.growth
        self._stats._grow_count += 1

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def display_stats(self) -> None:
        self._stats.display()

    @classmethod
    def create_plant(cls) -> "Plant":
        print("=== Anonymous")
        new_plant = cls("Unknown plan", 0.0, 0, 0.0)
        return new_plant

    @staticmethod
    def check_age(age: int) -> None:
        print(f"Is {age} more than a year? ->", end=" ")
        if age > 365:
            print(f"True")
        else:
            print("False")

    class Statistics:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, {self._age_count} age, {self._show_count} show")

class Flower(Plant):
    def __init__(self, name: str, height: int,
                 age: int, growth: float, color: str) -> None:
        super().__init__(name, height, age, growth)
        self.color = color
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed is True:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, growth: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age, growth)
        self.trunk_diameter = trunk_diameter
        self._stats = self.Statistics()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"{self.__class__.__name__} {self.name} now produces a shade of {self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide")
        self._stats._shade_count += 1

    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 growth: float, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age, growth)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def advance_day(self):
        self.advance_age()
        self.grow()
        self.nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int,
                 growth: float, color: str, seeds: int) -> None:
        super().__init__(name, height, age, growth, color)
        self.seeds = seeds

    def show(self) -> None:
        super().show()
        self.produce_seeds()
        print(f"Seeds: {self.seeds}")

    def produce_seeds(self) -> None:
        if self.bloomed is True:
            self.seeds = 42


def display_plant_stats(plant) -> None:
    plant.display_stats()

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print()
    print("=== Flower")
    plant1 = Flower("Rose", 15, 10, 8, "red")
    plant1.show()
    print(f"[statistics for {plant1.name}]")
    display_plant_stats(plant1)
    print(f"[asking the {plant1.name.lower()} to grow and bloom]")
    plant1.grow()
    plant1.bloom()
    plant1.show()
    print(f"[statistics for {plant1.name}]")
    display_plant_stats(plant1)
    print()
    print("===Tree")
    plant2 = Tree("Oak", 200, 365, 0.3, 5.0)
    plant2.show()
    print(f"[statistics for {plant2.name}]")
    display_plant_stats(plant2)
    plant2.produce_shade()
    print(f"[statistics for {plant2.name}]")
    display_plant_stats(plant2)
    print()
    print("=== Seed")
    plant3 = Seed("Sunflower", 80, 45, 1.5, "yellow", 0)
    plant3.show()
    print(f"[make {plant3.name.lower()} grow, age and bloom]")
    for day in range(20):
        plant3.advance_age()
        plant3.grow()
    plant3.bloom()
    plant3.show()
    print(f"[statistics for {plant3.name}]")
    display_plant_stats(plant3)
    print()
    plant4 = Plant.create_plant()
    plant4.show()
    print(f"[statistics for {plant4.name}]")
    display_plant_stats(plant4)
