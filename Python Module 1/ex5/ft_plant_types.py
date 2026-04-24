class Plant:
    def __init__(self, name: str, height: float,
                 age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._growth = 2.1

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def advance_age(self, days: int = 1) -> None:
        self._age += days

    def grow(self, days: int = 1) -> None:
        self._height = self._height + self._growth * days

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

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
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
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"{self.__class__.__name__} {self.name} now produces a"
              f" shade of {self._height:.1f}cm long "
              f"and {self.trunk_diameter:.1f}cm wide")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self, days: int = 1) -> None:
        super().grow(days)
        self.nutritional_value += days


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant1 = Flower("Rose", 15, 10, "red")
    plant1.show()
    plant1.bloom()
    plant1.show()
    print()
    print("=== Tree")
    plant2 = Tree("Oak", 200, 365, 5.0)
    plant2.show()
    plant2.produce_shade()
    print()
    print("=== Vegetable")
    plant3 = Vegetable("Tomato", 5, 10, "April", 0)
    plant3.show()
    number_days = 20
    print(f"[make tomato grow and age for {number_days} days]")
    plant3.advance_age(20)
    plant3.grow(20)
    plant3.show()
